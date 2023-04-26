from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest


def get_sessions(property_id):
    """Get sessions metric from Google Analytics 4 Data API"""
    client = BetaAnalyticsDataClient()
    request = RunReportRequest(
        property='properties/'+property_id,
        metrics=[Metric(name='sessions')],
        date_ranges=[DateRange(start_date="2022-04-24", end_date="today")])
    
    response = client.run_report(request)
    return response.rows[0].metric_values[0].value
