from dagster import execute_solid
from dagster_proj.pipelines.my_pipeline import MODE_TEST
from dagster_proj.solids.hello import hello


def test_hello():
    """
    This is an example test for a Dagster solid.

    For hints on how to test your Dagster solids, see our documentation tutorial on Testing:
    https://docs.dagster.io/tutorial/testable
    """
    result = execute_solid(hello, mode_def=MODE_TEST)

    assert result.success
    assert result.output_value() == "Hello, Dagster!"
