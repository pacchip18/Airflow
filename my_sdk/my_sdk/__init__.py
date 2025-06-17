from typing import List, Dict, Any

__version__ = "0.0.1"
__all__ = ["sql"]



def get_provider_info() -> Dict[str, Any]:
    return {
        "package-name": "my-sdk",
        "name": "My SDK",
        "description": "My SDK is a package that providers set of tools for building Airflow DAGs and tasks.",
        "versions": [__version__],
        "task-decorators": [
            {
                "name": "sql",
                "class-name": "my_sdk.decorators.sql.sql_task"
                
                }
        ]
    }