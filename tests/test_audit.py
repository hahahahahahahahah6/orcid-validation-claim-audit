import json
import tempfile
import unittest
from pathlib import Path
from orcid_validation_claim_audit.audit import audit, claims, evidence, main
from orcid_validation_claim_audit.phrases import GENERIC_NAMES, ORCIDVALIDATION, NOORCIDVALIDATION


class AuditTests(unittest.TestCase):
    def test_phrases(self):
        for phrase in ORCIDVALIDATION:
            with self.subTest(phrase=phrase):
                self.assertTrue(claims(phrase)[0])
        for phrase in NOORCIDVALIDATION:
            with self.subTest(phrase=phrase):
                self.assertEqual(claims(phrase)[0], set())
                self.assertTrue(claims(phrase)[1])
        self.assertEqual(claims('```\nvalidate orcid\n```'), (set(), set()))
        self.assertTrue(claims('`validate-orcid`')[0])
        self.assertTrue(claims("doesn't validate orcid")[1])

    def test_library_routes(self):
        routes = ['from idutils import is_orcid as f\nf(x)', 'from idutils.validators import is_orcid\nis_orcid(x)', 'import idutils as iu\niu.is_orcid(x)', 'from idutils import is_isni as f\nf(x)', 'from idutils.validators import is_isni\nis_isni(x)', 'import idutils\nidutils.is_isni(x)']
        for name in ('validate', 'is_valid'):
            routes += ['from stdnum.isni import %s as f\nf(x)' % name, 'import stdnum.isni\nstdnum.isni.%s(x)' % name, 'import stdnum.isni as si\nsi.%s(x)' % name, 'from stdnum import isni\nisni.%s(x)' % name]
        for source in routes:
            with self.subTest(source=source): self.assertTrue(evidence(source))

    def test_generic_routes(self):
        for name in GENERIC_NAMES:
            for source in ('obj.%s(x)' % name, 'from lib import %s as f\nf(x)' % name, 'obj = thing()\nobj.%s(x)' % name):
                with self.subTest(source=source): self.assertTrue(evidence(source))

    def test_not_evidence(self):
        cases = ['import idutils', 'is_orcid(x)', 'is_isni(x)', 'validate(x)', 'is_valid(x)', 'normalize_orcid(x)', 'validate_orcid(x)', 'obj.is_orcid(x)', 'obj.is_isni(x)', 'obj.validate(x)', 'obj.is_valid(x)', 'obj.normalize_orcid(x)', 'import idutils\nidutils.normalize_orcid(x)', 'import idutils\nidutils.normalize_isni(x)', 'from stdnum import isni\nisni.compact(x)', 'from stdnum import isni\nisni.format(x)', 'import idutils\nidutils.detect_identifier_schemes(x)', 'import orcid\norcid.Client().read(x)', 'import pyorcid\npyorcid.Client().read(x)', 'import re\nre.match(pattern, x)', 'import re\nre.search(pattern, x)', 'import re\nre.fullmatch(pattern, x)', '1 < x < 100', "x.removeprefix('https://orcid.org/')", 'import validators\nvalidators.orcid(x)', 'import stdnum.orcid\nstdnum.orcid.validate(x)', '"validate orcid"', '# validate orcid', 'obj.validate_orcid', 'def bad(:', 'import subprocess\nsubprocess.run(["orcid-check", x])', 'from idutils import is_orcid\ndef is_orcid(x): pass\nis_orcid(x)', 'import idutils\nidutils = other\nidutils.is_orcid(x)', 'from lib import validate_orcid\nwith ctx() as validate_orcid: pass\nvalidate_orcid(x)', 'def validate_orcid(x): pass\nobj.validate_orcid(x)']
        for source in cases:
            with self.subTest(source=source): self.assertFalse(evidence(source))

    def test_findings_and_scopes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root/'README.md').write_text('validate orcid')
            self.assertEqual(audit(root)[0]['severity'], 'HIGH')
            (root/'tests').mkdir(); (root/'tests/test_x.py').write_text('import idutils\nidutils.is_orcid(x)')
            self.assertEqual(audit(root)[0]['severity'], 'MEDIUM')
            (root/'app.py').write_text('import idutils\nidutils.is_orcid(x)')
            self.assertEqual(audit(root), [])
            (root/'README.md').write_text('does not validate orcid')
            self.assertEqual(audit(root)[0]['id'], 'documented-no-orcid-validation-claim-false')
            self.assertEqual(audit(root, ['app.py']), [])
            (root/'docs').mkdir(); (root/'docs/a.md').write_text('validate orcid')
            self.assertTrue(audit(root, ['app.py']))

    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root/'README.md').write_text('validate orcid')
            self.assertEqual(main(['audit', tmp, '--json']), 2)
            (root/'test_a.py').write_text('import idutils\nidutils.is_orcid(x)')
            self.assertEqual(main(['audit', tmp]), 0)
            self.assertEqual(main(['audit', tmp, '--fail-on', 'medium']), 2)
            self.assertEqual(main(['audit', tmp + '/missing']), 1)


if __name__ == '__main__': unittest.main()
