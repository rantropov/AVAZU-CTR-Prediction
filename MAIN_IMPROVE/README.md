IMPROVEMENTS BASED ON MAJOR PLANNING
===================

##### Step 1 FEATURE ENGINEERING
	- Features in test not in train
		1. First 3 digits in ID => geographical info
		2. Unseen variables => 'Other'(-2)

##### Step 2 SHUFFLE DATA
	../../shuf-t-master/shuf-t -t 1 train_df_app_smooth.csv -o train_df_app_smooth_shuffled.csv

###### Middle steps - vw format transformation

###### Middle steps - hashing / one-hot encoding

##### Step 3 VALIDATION (1.5%)

##### Step 4 SEPARATELY TUNING MODELS => Vowpal Wabbit

##### Step 5 SINGLE MODELS
	- libFM
		1. SGD
		2. MCMC
	- xgboost
		1. GBM
	- R/Python 
		1. SVM - batch (avg results)

##### Step 6 BLENDING
	- Weighted


###### fast solution python 
Unseen feature (not shuffled):<br>
	- 0.13 | 1 | 1 | 1 | 28 - local: 0.439512/0.306498 | LB: 0.3931091 (benchmark)<br>
	- 0.13 | 1 | 1 | 1 | 28 - local: 0.442022/0.310298 | LB: 0.3963906 (unseen test/train => -2)<br>
	- 0.13 | 1 | 1 | 1 | 28 - local: 0.439512/0.306498 | LB: 0.3957204 (unseen test => -2)<br>
	- 0.13 | 1 | 1 | 1 | 28 - local: 0.439512/0.306498 | LB: 0.3931100 (unseen test => '')<br>

Blending:<br>
	- xgboost 600_900 / python online | LB: 0.3912111<br>

Shuffled:<br>
	- 0.13 | 1 | 1 | 1 | 28 - local: 0.439533/0.309538 | LB: (unseen test => '')<br>
	- 0.13 | 1 | 1 | 1 | 28 - local: 0.440630/0.307406 | LB: (unseen test => '', seed=888)<br>







