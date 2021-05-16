from dagster import repository

from dagster_proj.pipelines.my_pipeline import my_pipeline
from dagster_proj.schedules.my_hourly_schedule import my_hourly_schedule
from dagster_proj.sensors.my_sensor import my_sensor


@repository
def dagster_proj():
    """
    The repository definition for this dagster_proj Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    pipelines = [my_pipeline]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return pipelines + schedules + sensors
