from .ingest_validation_tools.error_report import ErrorReport
from .ingest_validation_tools.upload import Upload
import json

from .ingest_validation_tools.schema_loader import PreflightError
from .ingest_validation_tools.validation_utils import (
    get_tsv_errors, get_table_schema_version
)

class ValidateUpload:
    def __init__(self):
        print('Validator ...')

    def validate_dir(self, directory_path=None):
        upload = Upload(directory_path=directory_path)
        report = ErrorReport(upload.get_errors())
        response = {
            "report": report
        }
        return json.dumps(response)

    def validate_tsvs(self, schema='metadata', path = None, output = None):
        try:
            schema_name = (
                schema if schema != 'metadata'
                else get_table_schema_version(path, 'ascii').schema_name
            )
        except PreflightError as e:
            errors = {'Preflight': str(e)}
        else:
            errors = get_tsv_errors(path, schema_name=schema_name)
            errors = {f'{schema_name} TSV errors': errors} if errors else {}
        report = ErrorReport(
            info={},  # Until we know it's needed, don't bother filling this in.
            errors=errors)
        return json.dumps(report)