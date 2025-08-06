from schema_parser import SchemaParser
from data_generator import DataGenerator
from validator import Validator
from exporter import Exporter

# Example usage
schema_file = "sample_schema.sql"
parser = SchemaParser(schema_file)
tables = parser.parse()

generator = DataGenerator(tables)
data = generator.generate()

validator = Validator(tables, data)
validator.run_checks()

exporter = Exporter(data)
exporter.to_csv()
