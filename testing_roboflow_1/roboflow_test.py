from dotenv import load_dotenv
load_dotenv()

import os
import roboflow

#@roboflow setup

roboflow_api_key = os.getenv('ROBOFLOW_API_KEY')

rf = roboflow.Roboflow(api_key=roboflow_api_key)

#@roboflow setup done


