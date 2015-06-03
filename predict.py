
from train import Training
from apiclient.errors import HttpError
from matplotlib import pyplot as plt
import numpy as np

class Prediction(Training):

    def start(self):
        try:
            self.make_prediction()
        except HttpError as e:
            if e.resp.status == 404:
                print("No Model found. Model must first be trained.")
            else:
                print(e)

    @staticmethod
    def plot_results(data):

        score = []
        label = []

        # iterate over output data and covert string to float and integer
        for item in data:
            for key in item:
                if key == 'score':
                    item[key] = float(item[key])
                    score.append(item[key])
                elif key == 'label':
                    item[key] = int(item[key])
                    label.append(item[key])

        # prepare parameters for plotting
        x = np.arange(len(data))
        max_index = score.index(max(score))
        explode = np.zeros(10)
        explode[max_index] = 0.1
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'c', 'm', 'y', 'g', 'b', 'r']

        # bar chart
        plt.subplot(1, 2, 1), plt.bar(x, score)
        plt.xticks(x + 0.5, label)

        # pie chart
        plt.subplot(1,2,2), plt.pie(score, explode=explode, labels=label, autopct='%1.1f%%',colors=colors)
        plt.axis('equal')

        plt.show()

    def make_prediction(self):

        model = self.prediction_service.trainedmodels().get(project=self.project_id, id=self.model_id).execute()

        if model.get('trainingStatus') == 'RUNNING':
            print("Training in progress, please wait and try again later.")

        elif model.get('trainingStatus') == 'DONE':
            print(model.get('trainingComplete'))

            # load local testing data
            with open('test_data/digit_0.txt') as f:
                record = f.readline().split(',')

            prediction = self.prediction_service.trainedmodels().predict(project=self.project_id, id=self.model_id, body={
                'input': {
                    'csvInstance': record
                },
            }).execute()

            # retrieve results
            output_label = prediction.get('outputLabel')
            output_multi = prediction.get('outputMulti')
            print output_label
            print output_multi

            # plot results
            self.plot_results(output_multi)

if __name__ == '__main__':
    Prediction().start()
