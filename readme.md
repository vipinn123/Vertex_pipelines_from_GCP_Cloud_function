This module demonstrates triggering a Vertex AI pipeline job using GCP Cloud Function

Create a cloud function in GCP

In the (1) Configuration tab
Set up the basics as below
-Environment = 1st gen
-Function name=pipeline-cloud-fn 
-Region = us-central1
Trigger Type = HTTP
Uncheck Require HTTPS
Runtime service account = compute engine default service account

In the (2) code tab
Select Runtime as Python 3.7
Entry point = hellow_world
Source code = Inline Editor

Copy the contents of the main.py in git into the main.py of the INline editor
Copy the the contents of requirements.txt into the requirements.txt of the inline editor


