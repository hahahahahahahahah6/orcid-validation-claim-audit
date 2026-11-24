# Researcher identifier claim audit

```text
orcid-validation-claim-audit
```

This offline static audit compares documented researcher-identifier capability claims with Python call shapes. It never executes inspected code or contacts a network. An ORCID iD has 16 characters, a MOD 11-2 check digit that can be X, and can be presented as an https://orcid.org/ URI.

## Usage

```sh
orcid-validation-claim-audit audit .
orcid-validation-claim-audit audit . --json --verbose --ignore vendor --fail-on medium
python3 -m orcid_validation_claim_audit --version
```

The optional path defaults to the current directory. Repeat `--ignore` for each path prefix. The default failure threshold is high; `--fail-on medium` includes test-only evidence. Exit status is 0 for a pass at the selected threshold, 2 for a finding at or above it, and 1 for usage or I/O errors.

The findings are:

```text
documented-orcid-validation-claim-false
documented-no-orcid-validation-claim-false
```

The first is high severity without production evidence and medium when evidence occurs only in tests. The second is high severity when a documented denial conflicts with production evidence. Root README and Markdown files under a docs directory are read; fenced blocks are excluded and inline code counts. Fixtures, docs, and examples are excluded from source evidence; tests are counted separately. Symlinks are skipped.

## Differentiation

Generic input validation checks whether input is checked at all; this audit does not cover that.

Isbn validation checks the isbn 10 or isbn 13 check digit of a book number; this audit does not cover that.

Issn validation checks the check digit of a serial number; this audit does not cover that.

Iban validation checks the check digit of a bank account number; this audit does not cover that.

Uuid validation checks the shape of a universally unique identifier; this audit does not cover that.

Semver validation checks the shape of a semantic version; this audit does not cover that.

Mac address validation checks a hardware address; this audit does not cover that.

Bic validation checks a bank identifier code; this audit does not cover that.

Cron expression validation checks a schedule string; this audit does not cover that.

Cron expression description turns a schedule string into a human readable sentence; this audit does not cover that.

Scheduled execution runs a job on a schedule; this audit does not cover that.

Date validation checks whether a date is a real calendar date; this audit does not cover that.

Timeouts limit how long a call may run; this audit does not cover that.

Payment processing takes a payment from a card; this audit does not cover that.

Credit card extraction reads card details from a document; this audit does not cover that.

Authentication can prove account ownership with a one time code or confirmation link; this audit does not cover that.

Password authentication verifies a password against a stored hash; this audit does not cover that.

Password hashing prepares a password for storage; this audit does not cover that.

Password generation mints a random password; this audit does not cover that.

Pdf encryption protects a pdf with a password; this audit does not cover that.

Email sending delivers mail; this audit does not cover that.

Sms sending delivers a text message; this audit does not cover that.

Document extraction reads data out of a document; this audit does not cover that.

Barcode scanning decodes a code from an image; this audit does not cover that.

Email validation judges an email address or its deliverability; this audit does not cover that.

Phone number validation judges a number or its validity for a region; this audit does not cover that.

Password strength evaluates how strong a password is; this audit does not cover that.

Json schema validation checks json data against a schema; this audit does not cover that.

Credit card validation judges a card number, its luhn check, and recognized brand; this audit does not cover that.

Domain validation checks a bare host name; this audit does not cover that.

Url validation checks a web address; this audit does not cover that.

Ip address validation checks a numeric address; this audit does not cover that.

Json decoding turns text into a value; this audit does not cover that.

Regex matching compares text with a pattern; this audit does not cover that.

Url parsing splits a web address into parts; this audit does not cover that.

Network fetching retrieves a web address; this audit does not cover that.

Dns resolution looks up a name; this audit does not cover that.

Barcode generation encodes an account number in a strip; this audit does not cover that.

Account number extraction reads a number from a document; this audit does not cover that.

Vehicle number extraction reads a number from a registration or image; this audit does not cover that.

Vehicle number decoding splits its sections or looks up make, model, and year; this audit does not cover that.

Vehicle history lookup asks a service about a number; this audit does not cover that.

Hex color validation judges a hexadecimal color string; this audit does not cover that.

Isni validation judges a 16 digit identifier without the researcher range check; this audit does not cover that.

Doi validation judges whether a digital object identifier names a work; this audit does not cover that.

Doi resolution asks whether a work identifier resolves; this audit does not cover that.

Record lookup fetches a researcher record from the registry; this audit does not cover that.

Researcher identifier extraction reads an identifier from a document; this audit does not cover that.

Spreadsheet reading is a separate claim family; this audit does not cover it.

Spreadsheet generation is a separate claim family; this audit does not cover it.

Word document reading is a separate claim family; this audit does not cover it.

Word document generation is a separate claim family; this audit does not cover it.

Presentation reading is a separate claim family; this audit does not cover it.

Presentation generation is a separate claim family; this audit does not cover it.

Pdf extraction is a separate claim family; this audit does not cover it.

Pdf generation is a separate claim family; this audit does not cover it.

Pdf merging is a separate claim family; this audit does not cover it.

Pdf splitting is a separate claim family; this audit does not cover it.

Pdf rotation is a separate claim family; this audit does not cover it.

Pdf form filling is a separate claim family; this audit does not cover it.

Pdf watermarking is a separate claim family; this audit does not cover it.

Pdf redaction is a separate claim family; this audit does not cover it.

Pdf compression is a separate claim family; this audit does not cover it.

Pdf annotation is a separate claim family; this audit does not cover it.

Table extraction is a separate claim family; this audit does not cover it.

Ocr is a separate claim family; this audit does not cover it.

Document extraction is a separate claim family; this audit does not cover it.

E signature is a separate claim family; this audit does not cover it.

Screen recording is a separate claim family; this audit does not cover it.

Video generation is a separate claim family; this audit does not cover it.

Qr code generation is a separate claim family; this audit does not cover it.

Barcode generation is a separate claim family; this audit does not cover it.

Barcode scanning is a separate claim family; this audit does not cover it.

Audio mixing is a separate claim family; this audit does not cover it.

Audio generation is a separate claim family; this audit does not cover it.

Audio editing is a separate claim family; this audit does not cover it.

Source separation is a separate claim family; this audit does not cover it.

Speech recognition is a separate claim family; this audit does not cover it.

Text to speech is a separate claim family; this audit does not cover it.

Noise suppression is a separate claim family; this audit does not cover it.

Music generation is a separate claim family; this audit does not cover it.

Music transcription is a separate claim family; this audit does not cover it.

## Limitations

```text
validate orcid
```
The bare phrase above can describe a manual runbook step, so it may trigger a false positive.

```text
orcid validation
```
The bare phrase above can describe a roadmap feature rather than implemented code.

```text
orcid validator
```
The bare phrase above can describe a hosted page instead of local code.

```text
orcid check
```
The bare phrase above can describe a field-presence rule instead of a shape judgement.

```text
check orcid
```
The bare phrase above can describe a manual runbook step.

```text
verify orcid
```
The bare phrase above can describe visually confirming a person's profile.

```text
orcid id validation
```
The bare phrase above can describe checking only whether a field is filled in.

```text
valid orcid
```
The bare phrase above can occur in example instructions without an implementation.

```text
orcid is valid
```
The bare phrase above can appear in example output without a call.

```text
orcid is invalid
```
The bare phrase above can appear in example error text without a call.

```text
orcid validity
```
The bare phrase above can name a configuration flag or column.

```text
orcid format validation
```
The bare phrase above can name a format description without code.

```text
validate orcid identifier
```
The bare phrase above can describe a manual runbook step.

```text
orcid identifier validation
```
The bare phrase above can name a specification section without code.

```text
orcid id check
```
The bare phrase above can name a checklist item without a call.

```text
check orcid id
```
The bare phrase above can describe a manual runbook step.

```text
validate orcid number
```
The bare phrase above can refer to generic ISNI structure rather than the reserved range.

```text
orcid number validation
```
The bare phrase above can name a specification section without code.

```text
validate orcid id
```
The bare phrase above can describe a manual runbook step.

```text
orcid validation
```
The bare phrase above can describe a result produced by an external service.

Bare imports are not evidence, even when the import is the only thing the module does.

A `.validate` call on a base that is not an `idutils` or `stdnum.isni` base is missed.

A route call must sit in a single module.

A route call on a name the module locally defines is shadowed.

A generic name called through an alias chain the tracer cannot follow is missed.

Dead code counts, because the audit reads code, not execution.

A subprocess call that shells out to an external checker is not evidence by design.

Syntax-invalid files give no evidence.

The audit matches exact phrases only, not meaning.

A doc that claims the checked capability in a roadmap, changelog, or TODO is still a claim.

A doc that denies the checked capability with a phrase outside the denial list is not recognised as a denial.

A claim in a file that is not the root README or under a docs path is not read at all.

A validation implementation in another language in the same repo is invisible.

A validation route that only exists at runtime, such as a dynamically imported module or a plugin loaded by name, is invisible.

This is static pattern matching, not a semantic judgement.

`normalize_orcid` only reformats and is not evidence.

`normalize_isni` only reformats and is not evidence.

`compact` only reformats and is not evidence.

`format` only reformats and is not evidence.

`detect_identifier_schemes` only classifies and is not evidence.

An API client call is a lookup and is not evidence.

A numeric range comparison alone is not evidence.

A URL-prefix strip alone is not evidence.

A regex match alone is not evidence.

The ISNI routes also accept generic ISNIs.

The X check digit is in scope.

The URI form is in scope.

Naming only the identifier does not constitute a claim.

A generic identifier check alone is insufficient.

A reference to a check digit alone is insufficient.

An ISNI structure call behind a researcher identifier claim is evidence by design.

A locally defined generic name is shadowed even when its implementation performs the check.

A result produced by an external platform is still flagged.

