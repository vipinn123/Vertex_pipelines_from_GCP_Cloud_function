from google.cloud import aiplatform

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()


    PROJECT_ID = '<your project name>'                     # <---CHANGE THIS
    REGION = 'us-central1'                             # <---CHANGE THIS
    PIPELINE_ROOT = '<your bucket>' # <---CHANGE THIS
    pipeline_spec_uri='full gcs path of where the compiled pipeline file is stored'
    
    #parameter_values = payload_json['parameter_values']

    # Create a PipelineJob using the compiled pipeline from pipeline_spec_uri
    aiplatform.init(
        project=PROJECT_ID,
        location=REGION,
    )
    job = aiplatform.PipelineJob(
        display_name='hello-world-pipeline-cloud-function-invocation',
        template_path=pipeline_spec_uri,
        pipeline_root=PIPELINE_ROOT,
        enable_caching=False,
        #parameter_values=parameter_values
    )

    job.submit()

    return job.job_id