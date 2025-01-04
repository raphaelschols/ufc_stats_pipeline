from itemadapter import ItemAdapter
from google.cloud import bigquery

class UfcStatsExamplePipeline:
    def __init__(self):
        # Initialize BigQuery client
        self.client = bigquery.Client(project="add_your_project_id").from_service_account_json( 
            "add_your_service_account_json_path"
        )  # Replace with your project ID


        # Set BigQuery dataset and table
        self.dataset_id = "ufc_data"  # Replace with your dataset ID
        self.table_id = "event_table"  # Target table name

    def process_item(self, item, spider):
        """
        Process and clean the item, and upload it to BigQuery.
        """
        adapter = ItemAdapter(item)
        cleaned_item = {key: value.strip() if isinstance(value, str) else value for key, value in adapter.items()}
        self.write_to_bigquery([cleaned_item])  # Wrap the item in a list for batch upload

        return item

    def write_to_bigquery(self, rows):
        """
        Write rows to BigQuery, creating the table if it doesn't exist.
        """
        # Define the table reference
        table_ref = self.client.dataset(self.dataset_id).table(self.table_id)

        # Check if the table exists; if not, create it
        try:
            self.client.get_table(table_ref)
        except Exception:
            print(f"Table {self.table_id} does not exist. Creating it...")
            self.create_table_with_autodetection(table_ref, rows)

        # Insert rows into the table
        job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
        load_job = self.client.load_table_from_json(rows, table_ref, job_config=job_config)
        load_job.result()  # Wait for the job to complete
        print(f"Rows successfully loaded into {self.table_id}.")

    def create_table_with_autodetection(self, table_ref, rows):
        """
        Create a BigQuery table with schema autodetection using the provided rows.
        """
        job_config = bigquery.LoadJobConfig(
            autodetect=True,  # Enable schema autodetection
            write_disposition="WRITE_EMPTY"
        )
        load_job = self.client.load_table_from_json(rows, table_ref, job_config=job_config)
        load_job.result()  # Wait for the job to complete
        print(f"Table {table_ref.table_id} created with autodetected schema.")
