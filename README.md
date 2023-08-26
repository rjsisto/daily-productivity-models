# Daily Productivity Models

## Project Description

This is a project done for a national food distributor in order to predict the daily productivity of a warehouse using various productivity metrics

## Installation and Setup

Follow these steps to get started:

1.  Clone this repository: `git clone https://github.com/rjsisto/daily-productivity-models.git`
2.  Open a terminal in the project directory: `cd daily-productivity-models`
3.  Create the virtual environment: `make env`
4.  Download the data: `make download_data`
5.  (Optional) Download the models:`make download_models`

## Usage

**Note:**  If running on Windows, use the `-w` argument to specify your OS
1.  Launch the Jupyter Notebooks: `make jup`
2.  Navigate to the notebooks folder to view the various notebooks
3.  In order to create the models for the dashboard without launching a Jupyter Notebook, run: `make build_models` (This processes the data and creates the models. This may take a little while.)
4.  Launch the dashboard (the dashboard will not run if the models have not been created): `make dash`

## Data and Preprocessing

The three datasets are sourced from the warehouses of a major food distributor. They contain information about the warehouses and daily metrics about how many hours were worked, how many cases were processed, and others. The data is somewhat randomized in order to prevent potentially important information from being shared. The preprocessing steps include merging all three datasets, dropping unneeded variables, and creating a main productivity metric (known as cases-per-man-hours). This main productivity metric was created by dividing the number of hours worked by the number of cases processed.

## Notebooks and Analysis

-   `data_preprocess.ipynb`: Merging the datasets, dropping unneeded variables, and creating the main productivity metric.

-   `model_build.ipynb`: Creating the different models attempting to predict warehouse productivity

-   `model_eval.ipynb`: Evaluating the different models using various metrics and visualizations

## Results and Visualizations

The table below shows the different model's performance at predicting warehouse productivity (the models did perform much better with the real data, instead of the randomized data).

![Model Metrics](notebooks/images/model_metrics.png)

We can also see that the most important variables in predicting warehouse productivity is the number of hours that cohort C worked and the number of cases that cohort A worked. Each warehouse is divided up into three cohorts (A, B, and C) based upon their experience working in the warehouse.

![Variable Importance](notebooks/images/gbr_feature_importance.png)

Finally, here is a screenshot of the interactive dashboard showing the real and predicted values graphed on top of each other.

![Dashboard Screenshot](notebooks/images/dashboard.png)

## Project Structure

-   `notebooks/`: Jupyter notebooks for data preprocessing, modeling, and analysis.
-   `notebooks/data/`: Contains the dataset files.
-   `notebooks/models/`: Folder where the models will be stored
-   `data_app/`: Contains the files for the dashboard app.

## Future Work

- Create a docker container for this project
- Create tests to ensure that all aspects of this project are running as intended

## Contact

For questions or suggestions, feel free to contact me at rjsisto1000\@gmail.com.
