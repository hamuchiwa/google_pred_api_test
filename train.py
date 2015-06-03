
import webbrowser
import httplib2
from apiclient import discovery
from oauth2client import client

class Training(object):

    def __init__(self):

        self.project_id = '529231445931'
        self.model_id = 'handwritten_digits_model'

        # authorization for installed application, "client_secrets.json" required
        flow = client.flow_from_clientsecrets(
            'client_secrets.json',
            scope = [
                'https://www.googleapis.com/auth/prediction',
                'https://www.googleapis.com/auth/devstorage.read_only'],
            redirect_uri='urn:ietf:wg:oauth:2.0:oob')

        auth_uri = flow.step1_get_authorize_url()
        webbrowser.open(auth_uri)
        auth_code = raw_input('Enter the auth code: ')
        credentials = flow.step2_exchange(auth_code)
        http_auth = credentials.authorize(httplib2.Http())
        self.prediction_service = discovery.build('prediction', 'v1.6', http=http_auth)

    def train_model(self):

        self.prediction_service.trainedmodels().insert(project=self.project_id, body={
            'id': self.model_id,
            'storageDataLocation': 'handwritten_digits/train_data.csv',
            'modelType': 'CLASSIFICATION'
        }).execute()

if __name__ == '__main__':
    Training().train_model()
