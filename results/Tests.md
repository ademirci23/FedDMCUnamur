Les valeurs dans le papier sont une moyenne sur 5 runs.

Test 1 : 
python main.py --byz_type GS_attack --agg_type pca_hdbscan_b --dataset mnist --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10
    - Results : 
    [INFO](2026/04/12/ 06:35:08 AM) agg_type: pca_hdbscan_b
[INFO](2026/04/12/ 06:35:09 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/04/12/ 06:35:09 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/04/12/ 06:35:09 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/04/12/ 06:35:09 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/04/12/ 06:35:09 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/04/12/ 06:35:09 AM) [Round: 199] >> Time of aggregation: 0.271932 s
[INFO](2026/04/12/ 06:35:09 AM) [Round: 199] >> Global Model Test accuracy: 0.980762
[INFO](2026/04/12/ 06:35:09 AM) [Round: 199] >> Global Model Test loss: 0.083456

Valeur dans la table 4 FEDDMC : 98.12, dans le test 98.07 : Presque pareil. 

Test 2 : 
python main.py --dataset mnist --byz_type LF_attack --agg_type foolsgold --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 
 - Results : 
 [INFO](2026/04/12/ 05:12:17 PM) agg_type: foolsgold
[INFO](2026/04/12/ 05:12:17 PM) [Round: 199] >> Detect_malicious_client: ['client5', 'client6', 'client7', 'client10', 'client11', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client36', 'client37', 'client38', 'client39', 'client42', 'client43', 'client45', 'client46', 'client47', 'client52', 'client53', 'client54', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client80', 'client81', 'client82', 'client87', 'client88', 'client89', 'client90', 'client91', 'client95', 'client96']
[INFO](2026/04/12/ 05:12:17 PM) [Round: 199] >> Number_malicious_client: 40
[INFO](2026/04/12/ 05:12:17 PM) [Round: 199] >> Server Defense accuracy: 0.320000
[INFO](2026/04/12/ 05:12:17 PM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/04/12/ 05:12:17 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/04/12/ 05:12:17 PM) [Round: 199] >> Time of aggregation: 0.157771 s
[INFO](2026/04/12/ 05:12:18 PM) [Round: 199] >> Global Model Test accuracy: 0.427734
[INFO](2026/04/12/ 05:12:18 PM) [Round: 199] >> Global Model Test loss: 0.898102


Valeur dans la table 4 FEDDMC : 28.94, dans le test 42.77 : Grosse différence.

Test 3 : 
python main.py --dataset mnist --byz_type LIT_attack --agg_type multi_krum --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10
______
Valeur dans la table 4 FEDDMC : 8.81, dans le test : 55-60 average
-> Grosse différence, car j'ai lancé avec IID = TRUE, dans la papier, c'est indiqué q'ils lancent avec IID = false.
Test 3 redone with : 
python main.py --dataset mnist --byz_type LIT_attack --agg_type multi_krum --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10
TACC ≈ 87.16
ASR ≈ 8.81%
[INFO](2026/04/14/ 02:07:40 AM) agg_type: multi_krum
[INFO](2026/04/14/ 02:07:41 AM) [Round: 199] >> Detect_malicious_client: ['client7', 'client86', 'client81', 'client89', 'client27', 'client46', 'client31', 'client59', 'client30', 'client88', 'client6', 'client87', 'client25', 'client35', 'client44', 'client43', 'client45', 'client33', 'client37', 'client24', 'client5', 'client36', 'client4', 'client42', 'client41', 'client39', 'client38', 'client1']
[INFO](2026/04/14/ 02:07:41 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/04/14/ 02:07:41 AM) [Round: 199] >> Server Defense accuracy: 0.440000
[INFO](2026/04/14/ 02:07:41 AM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/04/14/ 02:07:41 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/04/14/ 02:07:41 AM) [Round: 199] >> Time of aggregation: 0.140324 s
[INFO](2026/04/14/ 02:07:44 AM) [Round: 199] >> Global ASR: 0.827300
[INFO](2026/04/14/ 02:07:44 AM) [Round: 199] >> Global Model Test accuracy: 0.974023
[INFO](2026/04/14/ 02:07:44 AM) [Round: 199] >> Global Model Test loss: 0.094281

RUN 2 : 

[INFO](2026/04/13/ 12:42:43 PM) agg_type: multi_krum
[INFO](2026/04/13/ 12:42:43 PM) [Round: 199] >> Detect_malicious_client: ['client61', 'client82', 'client59', 'client4', 'client58', 'client81', 'client56', 'client86', 'client93', 'client78', 'client80', 'client94', 'client95', 'client1', 'client87', 'client54', 'client79', 'client91', 'client50', 'client88', 'client90', 'client53', 'client51', 'client89', 'client98', 'client99', 'client52', 'client96']
[INFO](2026/04/13/ 12:42:43 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/04/13/ 12:42:43 PM) [Round: 199] >> Server Defense accuracy: 0.440000
[INFO](2026/04/13/ 12:42:43 PM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/04/13/ 12:42:43 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/04/13/ 12:42:43 PM) [Round: 199] >> Time of aggregation: 0.131068 s
[INFO](2026/04/13/ 12:42:45 PM) [Round: 199] >> Global ASR: 0.568200
[INFO](2026/04/13/ 12:42:45 PM) [Round: 199] >> Global Model Test accuracy: 0.975000
[INFO](2026/04/13/ 12:42:45 PM) [Round: 199] >> Global Model Test loss: 0.089226

RUN 3 : 

[INFO](2026/04/13/ 12:39:21 PM) agg_type: multi_krum
[INFO](2026/04/13/ 12:39:22 PM) [Round: 199] >> Detect_malicious_client: ['client61', 'client58', 'client86', 'client64', 'client54', 'client50', 'client88', 'client71', 'client51', 'client53', 'client87', 'client90', 'client52', 'client89', 'client1', 'client70', 'client65', 'client96', 'client93', 'client66', 'client99', 'client68', 'client91', 'client98', 'client69', 'client94', 'client95', 'client67']
[INFO](2026/04/13/ 12:39:22 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/04/13/ 12:39:22 PM) [Round: 199] >> Server Defense accuracy: 0.440000
[INFO](2026/04/13/ 12:39:22 PM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/04/13/ 12:39:22 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/04/13/ 12:39:22 PM) [Round: 199] >> Time of aggregation: 0.900150 s
[INFO](2026/04/13/ 12:39:27 PM) [Round: 199] >> Global ASR: 0.551600
[INFO](2026/04/13/ 12:39:27 PM) [Round: 199] >> Global Model Test accuracy: 0.973730
[INFO](2026/04/13/ 12:39:27 PM) [Round: 199] >> Global Model Test loss: 0.088770

Run 4 : 

[INFO](2026/04/13/ 12:40:09 PM) agg_type: multi_krum
[INFO](2026/04/13/ 12:40:09 PM) [Round: 199] >> Detect_malicious_client: ['client5', 'client43', 'client86', 'client78', 'client4', 'client50', 'client44', 'client51', 'client42', 'client54', 'client87', 'client80', 'client1', 'client52', 'client93', 'client81', 'client94', 'client98', 'client91', 'client95', 'client79', 'client82', 'client99', 'client96', 'client53', 'client90', 'client88', 'client89']
[INFO](2026/04/13/ 12:40:09 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/04/13/ 12:40:09 PM) [Round: 199] >> Server Defense accuracy: 0.440000
[INFO](2026/04/13/ 12:40:09 PM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/04/13/ 12:40:09 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/04/13/ 12:40:09 PM) [Round: 199] >> Time of aggregation: 0.220362 s
[INFO](2026/04/13/ 12:40:13 PM) [Round: 199] >> Global ASR: 0.600400
[INFO](2026/04/13/ 12:40:13 PM) [Round: 199] >> Global Model Test accuracy: 0.974902
[INFO](2026/04/13/ 12:40:13 PM) [Round: 199] >> Global Model Test loss: 0.087759

RUN 5 : 

[INFO](2026/04/13/ 12:33:57 PM) agg_type: multi_krum
[INFO](2026/04/13/ 12:33:58 PM) [Round: 199] >> Detect_malicious_client: ['client64', 'client54', 'client66', 'client84', 'client50', 'client53', 'client82', 'client5', 'client4', 'client98', 'client78', 'client51', 'client1', 'client52', 'client96', 'client81', 'client95', 'client99', 'client94', 'client86', 'client93', 'client91', 'client80', 'client79', 'client88', 'client89', 'client90', 'client87']
[INFO](2026/04/13/ 12:33:58 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/04/13/ 12:33:58 PM) [Round: 199] >> Server Defense accuracy: 0.440000
[INFO](2026/04/13/ 12:33:58 PM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/04/13/ 12:33:58 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/04/13/ 12:33:58 PM) [Round: 199] >> Time of aggregation: 1.146732 s
[INFO](2026/04/13/ 12:34:03 PM) [Round: 199] >> Global ASR: 0.600400
[INFO](2026/04/13/ 12:34:03 PM) [Round: 199] >> Global Model Test accuracy: 0.976953
[INFO](2026/04/13/ 12:34:03 PM) [Round: 199] >> Global Model Test loss: 0.081638

____________________________
Test 4 : 
python main.py --dataset mnist --byz_type LIT_attack --agg_type auror --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01
Résultat attendu (Table IV du paper, moyenne sur 5 runs) :
TACC ≈ 98.07%
ASR ≈ 5.75%
- Results : 
[INFO](2026/04/14/ 02:48:03 AM) agg_type: auror
[INFO](2026/04/14/ 02:48:03 AM) [Round: 199] >> Detect_malicious_client: ['client1']
[INFO](2026/04/14/ 02:48:03 AM) [Round: 199] >> Number_malicious_client: 1
[INFO](2026/04/14/ 02:48:03 AM) [Round: 199] >> Server Defense accuracy: 0.710000
[INFO](2026/04/14/ 02:48:03 AM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/04/14/ 02:48:03 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/04/14/ 02:48:03 AM) [Round: 199] >> Time of aggregation: 0.250896 s
[INFO](2026/04/14/ 02:48:05 AM) [Round: 199] >> Global ASR: 0.505100
[INFO](2026/04/14/ 02:48:05 AM) [Round: 199] >> Global Model Test accuracy: 0.978320
[INFO](2026/04/14/ 02:48:05 AM) [Round: 199] >> Global Model Test loss: 0.077430



Test 5 : 
python main.py --dataset mnist --byz_type LIT_attack --agg_type foolsgold --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01
Résultat attendu (Table IV) :
TACC ≈ 98.00%
ASR ≈ 41.59%
- Results : 
[INFO](2026/04/14/ 02:40:52 AM) agg_type: foolsgold
[INFO](2026/04/14/ 02:40:52 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client1', 'client2', 'client3', 'client4', 'client5', 'client6', 'client7', 'client8', 'client9', 'client10', 'client11', 'client12', 'client13', 'client14', 'client15', 'client17', 'client18', 'client19', 'client20', 'client21', 'client22', 'client23', 'client26', 'client27', 'client28', 'client29', 'client30', 'client31', 'client32', 'client34', 'client36', 'client37', 'client38', 'client39', 'client40', 'client41', 'client42', 'client43', 'client44', 'client45', 'client46', 'client47', 'client48', 'client49', 'client50', 'client51', 'client52', 'client53', 'client54', 'client55', 'client56', 'client57', 'client58', 'client59', 'client60', 'client61', 'client62', 'client63', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client72', 'client74', 'client75', 'client77', 'client78', 'client79', 'client80', 'client83', 'client84', 'client85', 'client86', 'client87', 'client88', 'client89', 'client90', 'client92', 'client93', 'client94', 'client95', 'client96', 'client97', 'client98', 'client99']
[INFO](2026/04/14/ 02:40:52 AM) [Round: 199] >> Number_malicious_client: 88
[INFO](2026/04/14/ 02:40:52 AM) [Round: 199] >> Server Defense accuracy: 0.400000
[INFO](2026/04/14/ 02:40:52 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/04/14/ 02:40:52 AM) [Round: 199] >> Server Detect malicious Recall: 0.318182
[INFO](2026/04/14/ 02:40:52 AM) [Round: 199] >> Time of aggregation: 0.136279 s
[INFO](2026/04/14/ 02:40:55 AM) [Round: 199] >> Global ASR: 0.600600
[INFO](2026/04/14/ 02:40:55 AM) [Round: 199] >> Global Model Test accuracy: 0.971973
[INFO](2026/04/14/ 02:40:55 AM) [Round: 199] >> Global Model Test loss: 0.104728







TEST 6 : 
python main.py --dataset mnist --byz_type LIT_attack --agg_type FLDetector --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10
Résultat attendu (Table IV) :
TACC ≈ 97.06
ASR ≈ 60.30
- Results : 
[INFO](2026/04/14/ 04:19:30 PM) agg_type: average
[INFO](2026/04/14/ 04:19:30 PM) [Round: 199] >> Detect_malicious_client: {}
[INFO](2026/04/14/ 04:19:30 PM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/04/14/ 04:19:30 PM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/04/14/ 04:19:30 PM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/04/14/ 04:19:30 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/04/14/ 04:19:30 PM) [Round: 199] >> Time of aggregation: 0.089398 s
[INFO](2026/04/14/ 04:19:34 PM) [Round: 199] >> Global ASR: 0.490000
[INFO](2026/04/14/ 04:19:34 PM) [Round: 199] >> Global Model Test accuracy: 0.976660
[INFO](2026/04/14/ 04:19:34 PM) [Round: 199] >> Global Model Test loss: 0.077493

-> FL_DETECTOR NOT IMPLEMENTED IN main.py


TEST 7 : 
python main.py --dataset mnist --byz_type LIT_attack --agg_type pca_hdbscan_b --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10
Résultat attendu (Table IV) :
TACC ≈ 98.10%
ASR ≈ 0.34
- Results :
[INFO](2026/04/14/ 04:20:43 PM) agg_type: pca_hdbscan_b
[INFO](2026/04/14/ 04:20:43 PM) [Round: 199] >> Detect_malicious_client: ['client0', 'client1', 'client2', 'client3', 'client8', 'client12', 'client13', 'client14', 'client15', 'client16', 'client17', 'client26', 'client29', 'client32', 'client34', 'client35', 'client36', 'client37', 'client38', 'client39', 'client40', 'client41', 'client42', 'client48', 'client49', 'client50', 'client51', 'client52', 'client53', 'client54', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client79', 'client80', 'client81', 'client82', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/04/14/ 04:20:43 PM) [Round: 199] >> Number_malicious_client: 47
[INFO](2026/04/14/ 04:20:43 PM) [Round: 199] >> Server Defense accuracy: 0.810000
[INFO](2026/04/14/ 04:20:43 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/04/14/ 04:20:43 PM) [Round: 199] >> Server Detect malicious Recall: 0.595745
[INFO](2026/04/14/ 04:20:43 PM) [Round: 199] >> Time of aggregation: 0.233517 s
[INFO](2026/04/14/ 04:20:45 PM) [Round: 199] >> Global ASR: 0.003900
[INFO](2026/04/14/ 04:20:45 PM) [Round: 199] >> Global Model Test accuracy: 0.978906
[INFO](2026/04/14/ 04:20:45 PM) [Round: 199] >> Global Model Test loss: 0.076160

-> GOOD


TEST 8 :

python main.py --dataset mnist --byz_type Scaling_attack --agg_type pca_hdbscan_b --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10
Résultat attendu (Table IV) :
TACC ≈ 98.06
ASR ≈ 54.51

[INFO](2026/04/15/ 05:22:12 AM) agg_type: pca_hdbscan_b
[INFO](2026/04/15/ 05:22:12 AM) [Round: 199] >> Detect_malicious_client: []
[INFO](2026/04/15/ 05:22:12 AM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/04/15/ 05:22:12 AM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/04/15/ 05:22:12 AM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/04/15/ 05:22:12 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/04/15/ 05:22:12 AM) [Round: 199] >> Time of aggregation: 0.317049 s
[INFO](2026/04/15/ 05:22:15 AM) [Round: 199] >> Global ASR: 0.902000
[INFO](2026/04/15/ 05:22:15 AM) [Round: 199] >> Global Model Test accuracy: 0.980957
[INFO](2026/04/15/ 05:22:15 AM) [Round: 199] >> Global Model Test loss: 0.077808
asr à 90%, ne match pas bien

RUN 2 : 

[INFO](2026/04/15/ 05:22:20 AM) agg_type: pca_hdbscan_b
[INFO](2026/04/15/ 05:22:20 AM) [Round: 199] >> Detect_malicious_client: []
[INFO](2026/04/15/ 05:22:20 AM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/04/15/ 05:22:20 AM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/04/15/ 05:22:20 AM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/04/15/ 05:22:20 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/04/15/ 05:22:20 AM) [Round: 199] >> Time of aggregation: 0.294518 s
[INFO](2026/04/15/ 05:22:23 AM) [Round: 199] >> Global ASR: 0.902000
[INFO](2026/04/15/ 05:22:23 AM) [Round: 199] >> Global Model Test accuracy: 0.982910
[INFO](2026/04/15/ 05:22:23 AM) [Round: 199] >> Global Model Test loss: 0.086210
asr à 90%, ne match pas bien
soucis peut venir d'ici : clip_rate = (num_in_comm / len(malicious_clients)) / 2



python main.py --dataset mnist --byz_type Scaling_attack --agg_type pca_hdbscan_b --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client
 28 --learning_rate 0.01 --pca_d 10


[INFO](2026/04/17/ 06:41:59 PM) agg_type: pca_hdbscan_b
[INFO](2026/04/17/ 06:41:59 PM) [Round: 199] >> Detect_malicious_client: []
[INFO](2026/04/17/ 06:41:59 PM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/04/17/ 06:41:59 PM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/04/17/ 06:41:59 PM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/04/17/ 06:41:59 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/04/17/ 06:41:59 PM) [Round: 199] >> Time of aggregation: 0.265185 s
[INFO](2026/04/17/ 06:42:02 PM) [Round: 199] >> Global ASR: 0.902000
[INFO](2026/04/17/ 06:42:02 PM) [Round: 199] >> Global Model Test accuracy: 0.959766
[INFO](2026/04/17/ 06:42:02 PM) [Round: 199] >> Global Model Test loss: 0.170109


 python main.py --dataset mnist --byz_type LIT_attack --agg_type foolsgold --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01

RUN 1 : 
 [INFO](2026/04/18/ 10:19:40 AM) agg_type: foolsgold
[INFO](2026/04/18/ 10:19:40 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client4', 'client5', 'client6', 'client7', 'client8', 'client9', 'client10', 'client11', 'client12', 'client13', 'client14', 'client15', 'client17', 'client18', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client26', 'client27', 'client28', 'client29', 'client30', 'client31', 'client32', 'client33', 'client34', 'client37', 'client38', 'client39', 'client40', 'client41', 'client42', 'client43', 'client44', 'client45', 'client46', 'client47', 'client48', 'client49', 'client50', 'client51', 'client52', 'client53', 'client54', 'client55', 'client56', 'client57', 'client58', 'client59', 'client60', 'client61', 'client62', 'client63', 'client64', 'client65', 'client66', 'client69', 'client70', 'client71', 'client72', 'client73', 'client74', 'client75', 'client76', 'client77', 'client78', 'client79', 'client80', 'client81', 'client82', 'client83', 'client84', 'client85', 'client86', 'client87', 'client88', 'client89', 'client90', 'client91', 'client92', 'client93', 'client94', 'client97', 'client98', 'client99']
[INFO](2026/04/18/ 10:19:40 AM) [Round: 199] >> Number_malicious_client: 92
[INFO](2026/04/18/ 10:19:40 AM) [Round: 199] >> Server Defense accuracy: 0.360000
[INFO](2026/04/18/ 10:19:40 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/04/18/ 10:19:40 AM) [Round: 199] >> Server Detect malicious Recall: 0.304348
[INFO](2026/04/18/ 10:19:40 AM) [Round: 199] >> Time of aggregation: 0.107221 s
[INFO](2026/04/18/ 10:19:43 AM) [Round: 199] >> Global ASR: 0.199400
[INFO](2026/04/18/ 10:19:43 AM) [Round: 199] >> Global Model Test accuracy: 0.965820
[INFO](2026/04/18/ 10:19:43 AM) [Round: 199] >> Global Model Test loss: 0.118166

RUN 2 : 
[INFO](2026/04/18/ 10:19:20 AM) agg_type: foolsgold
[INFO](2026/04/18/ 10:19:20 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client1', 'client2', 'client3', 'client4', 'client5', 'client6', 'client7', 'client8', 'client9', 'client10', 'client11', 'client12', 'client13', 'client15', 'client17', 'client18', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client26', 'client27', 'client28', 'client29', 'client30', 'client31', 'client32', 'client33', 'client34', 'client35', 'client36', 'client37', 'client38', 'client39', 'client40', 'client41', 'client42', 'client43', 'client44', 'client45', 'client46', 'client47', 'client48', 'client49', 'client50', 'client51', 'client52', 'client53', 'client54', 'client55', 'client56', 'client57', 'client58', 'client59', 'client60', 'client61', 'client62', 'client63', 'client64', 'client65', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client72', 'client73', 'client74', 'client75', 'client77', 'client78', 'client79', 'client80', 'client81', 'client82', 'client83', 'client84', 'client85', 'client88', 'client89', 'client90', 'client91', 'client92', 'client93', 'client94', 'client95', 'client96', 'client97', 'client98', 'client99']
[INFO](2026/04/18/ 10:19:20 AM) [Round: 199] >> Number_malicious_client: 95
[INFO](2026/04/18/ 10:19:20 AM) [Round: 199] >> Server Defense accuracy: 0.330000
[INFO](2026/04/18/ 10:19:20 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/04/18/ 10:19:20 AM) [Round: 199] >> Server Detect malicious Recall: 0.294737
[INFO](2026/04/18/ 10:19:20 AM) [Round: 199] >> Time of aggregation: 0.127568 s
[INFO](2026/04/18/ 10:19:23 AM) [Round: 199] >> Global ASR: 0.255600
[INFO](2026/04/18/ 10:19:23 AM) [Round: 199] >> Global Model Test accuracy: 0.964844
[INFO](2026/04/18/ 10:19:23 AM) [Round: 199] >> Global Model Test loss: 0.126575


python main.py --dataset mnist --byz_type LF_attack --agg_type pca_hdbscan_b --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10  

RUN 1 : 

[INFO](2026/06/18/ 09:26:51 AM) agg_type: pca_hdbscan_b
[INFO](2026/06/18/ 09:26:52 AM) [Round: 199] >> Detect_malicious_client: ['client9', 'client12', 'client17', 'client26', 'client27', 'client30', 'client32', 'client33', 'client40', 'client48', 'client62', 'client72', 'client73', 'client74', 'client76', 'client77', 'client78', 'client83', 'client84', 'client85', 'client92', 'client93', 'client98']
[INFO](2026/06/18/ 09:26:52 AM) [Round: 199] >> Number_malicious_client: 23
[INFO](2026/06/18/ 09:26:52 AM) [Round: 199] >> Server Defense accuracy: 0.750000
[INFO](2026/06/18/ 09:26:52 AM) [Round: 199] >> Server Detect malicious Precision: 0.464286
[INFO](2026/06/18/ 09:26:52 AM) [Round: 199] >> Server Detect malicious Recall: 0.565217
[INFO](2026/06/18/ 09:26:52 AM) [Round: 199] >> Time of aggregation: 0.234251 s
[INFO](2026/06/18/ 09:26:52 AM) [Round: 199] >> Global Model Test accuracy: 0.948242
[INFO](2026/06/18/ 09:26:52 AM) [Round: 199] >> Global Model Test loss: 0.370789


RUN 2 : 

[INFO](2026/06/18/ 09:26:15 AM) agg_type: pca_hdbscan_b
[INFO](2026/06/18/ 09:26:15 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client1', 'client2', 'client3', 'client4', 'client8', 'client9', 'client12', 'client13', 'client14', 'client15', 'client16', 'client17', 'client18', 'client26', 'client27', 'client29', 'client30', 'client32', 'client33', 'client34', 'client35', 'client40', 'client41', 'client48', 'client49', 'client50', 'client55', 'client56', 'client57', 'client58', 'client60', 'client61', 'client62', 'client63', 'client64', 'client72', 'client73', 'client74', 'client75', 'client76', 'client77', 'client78', 'client83', 'client84', 'client85', 'client86', 'client92', 'client93', 'client97', 'client98']
[INFO](2026/06/18/ 09:26:15 AM) [Round: 199] >> Number_malicious_client: 51
[INFO](2026/06/18/ 09:26:15 AM) [Round: 199] >> Server Defense accuracy: 0.770000
[INFO](2026/06/18/ 09:26:15 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/18/ 09:26:15 AM) [Round: 199] >> Server Detect malicious Recall: 0.549020
[INFO](2026/06/18/ 09:26:15 AM) [Round: 199] >> Time of aggregation: 0.302676 s
[INFO](2026/06/18/ 09:26:17 AM) [Round: 199] >> Global Model Test accuracy: 0.971484
[INFO](2026/06/18/ 09:26:17 AM) [Round: 199] >> Global Model Test loss: 0.138122


python main.py --dataset mnist --byz_type LF_attack --agg_type average --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

RUN 1 : 

[INFO](2026/06/18/ 09:26:27 AM) agg_type: average
[INFO](2026/06/18/ 09:26:27 AM) [Round: 199] >> Detect_malicious_client: {}
[INFO](2026/06/18/ 09:26:27 AM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/06/18/ 09:26:27 AM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/06/18/ 09:26:27 AM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/06/18/ 09:26:27 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/06/18/ 09:26:27 AM) [Round: 199] >> Time of aggregation: 0.083838 s
[INFO](2026/06/18/ 09:26:28 AM) [Round: 199] >> Global Model Test accuracy: 0.850781
[INFO](2026/06/18/ 09:26:28 AM) [Round: 199] >> Global Model Test loss: 0.513828

-----------

[INFO](2026/06/18/ 11:32:49 AM) {'debug': False, 'byz_type': 'LF_attack', 'agg_type': 'pca_hdbscan_b', 'dataset': 'mnist', 'epoch': 1, 'pca_d': 10, 'IID': False, 'beta': 5.0, 'num_of_clients': 100, 'num_malicious_client': 28, 'cfraction': 1, 'learning_rate': 0.01, 'logdir': './logs/', 'datadir': './data/', 'load_model_file': None, 'load_model_round': 0, 'tb_port': 6008}

RUN 1 : 

[INFO](2026/06/18/ 07:11:42 PM) agg_type: pca_hdbscan_b
[INFO](2026/06/18/ 07:11:42 PM) [Round: 199] >> Detect_malicious_client: ['client0', 'client1', 'client2', 'client3', 'client4', 'client8', 'client9', 'client12', 'client13', 'client14', 'client15', 'client16', 'client17', 'client18', 'client26', 'client27', 'client29', 'client30', 'client32', 'client33', 'client34', 'client35', 'client40', 'client48', 'client49', 'client50', 'client55', 'client56', 'client57', 'client58', 'client60', 'client61', 'client62', 'client63', 'client64', 'client72', 'client73', 'client74', 'client75', 'client76', 'client77', 'client83', 'client84', 'client85', 'client86', 'client92', 'client97', 'client98']
[INFO](2026/06/18/ 07:11:42 PM) [Round: 199] >> Number_malicious_client: 48
[INFO](2026/06/18/ 07:11:42 PM) [Round: 199] >> Server Defense accuracy: 0.800000
[INFO](2026/06/18/ 07:11:42 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/18/ 07:11:42 PM) [Round: 199] >> Server Detect malicious Recall: 0.583333
[INFO](2026/06/18/ 07:11:42 PM) [Round: 199] >> Time of aggregation: 0.215987 s
[INFO](2026/06/18/ 07:11:43 PM) [Round: 199] >> Global Model Test accuracy: 0.971680
[INFO](2026/06/18/ 07:11:43 PM) [Round: 199] >> Global Model Test loss: 0.152609



RUN 2 : 

[INFO](2026/06/18/ 07:10:27 PM) agg_type: pca_hdbscan_b
[INFO](2026/06/18/ 07:10:27 PM) [Round: 199] >> Detect_malicious_client: ['client8', 'client9', 'client12', 'client18', 'client27', 'client29', 'client30', 'client32', 'client33', 'client35', 'client40', 'client41', 'client50', 'client64', 'client72', 'client73', 'client74', 'client76', 'client78', 'client84', 'client86', 'client92', 'client93', 'client97', 'client98']
[INFO](2026/06/18/ 07:10:27 PM) [Round: 199] >> Number_malicious_client: 25
[INFO](2026/06/18/ 07:10:27 PM) [Round: 199] >> Server Defense accuracy: 0.650000
[INFO](2026/06/18/ 07:10:27 PM) [Round: 199] >> Server Detect malicious Precision: 0.321429
[INFO](2026/06/18/ 07:10:27 PM) [Round: 199] >> Server Detect malicious Recall: 0.360000
[INFO](2026/06/18/ 07:10:27 PM) [Round: 199] >> Time of aggregation: 0.309087 s
[INFO](2026/06/18/ 07:10:28 PM) [Round: 199] >> Global Model Test accuracy: 0.953711
[INFO](2026/06/18/ 07:10:28 PM) [Round: 199] >> Global Model Test loss: 0.366914



python main.py --dataset mnist --byz_type LF_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

RUN 1 : 

[INFO](2026/06/18/ 09:03:14 PM) agg_type: pca_agglomer_a
[INFO](2026/06/18/ 09:03:14 PM) [Round: 199] >> Detect_malicious_client: ['client5', 'client6', 'client7', 'client10', 'client11', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client28', 'client31', 'client36', 'client37', 'client38', 'client42', 'client43', 'client44', 'client45', 'client46', 'client47', 'client51', 'client52', 'client53', 'client54', 'client59', 'client65', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client79', 'client80', 'client81', 'client82', 'client87', 'client88', 'client89', 'client90', 'client91', 'client94', 'client95', 'client96', 'client99']
[INFO](2026/06/18/ 09:03:14 PM) [Round: 199] >> Number_malicious_client: 48
[INFO](2026/06/18/ 09:03:14 PM) [Round: 199] >> Server Defense accuracy: 0.240000
[INFO](2026/06/18/ 09:03:14 PM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/06/18/ 09:03:14 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/06/18/ 09:03:14 PM) [Round: 199] >> Time of aggregation: 0.232480 s
[INFO](2026/06/18/ 09:03:15 PM) [Round: 199] >> Global Model Test accuracy: 0.410937
[INFO](2026/06/18/ 09:03:15 PM) [Round: 199] >> Global Model Test loss: 0.898777

RUN 2 : 

[INFO](2026/06/19/ 06:11:05 AM) agg_type: pca_agglomer_a
[INFO](2026/06/19/ 06:11:05 AM) [Round: 199] >> Detect_malicious_client: ['client5', 'client6', 'client7', 'client10', 'client11', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client28', 'client31', 'client36', 'client37', 'client38', 'client43', 'client44', 'client45', 'client46', 'client47', 'client51', 'client52', 'client53', 'client54', 'client59', 'client65', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client79', 'client80', 'client81', 'client82', 'client87', 'client88', 'client89', 'client90', 'client91', 'client94', 'client95', 'client96', 'client99']
[INFO](2026/06/19/ 06:11:05 AM) [Round: 199] >> Number_malicious_client: 47
[INFO](2026/06/19/ 06:11:05 AM) [Round: 199] >> Server Defense accuracy: 0.250000
[INFO](2026/06/19/ 06:11:05 AM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/06/19/ 06:11:05 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/06/19/ 06:11:05 AM) [Round: 199] >> Time of aggregation: 0.277887 s
[INFO](2026/06/19/ 06:11:06 AM) [Round: 199] >> Global Model Test accuracy: 0.425098
[INFO](2026/06/19/ 06:11:06 AM) [Round: 199] >> Global Model Test loss: 0.909215


RUN 3 : 

[INFO](2026/06/19/ 06:10:08 AM) agg_type: pca_agglomer_a
[INFO](2026/06/19/ 06:10:08 AM) [Round: 199] >> Detect_malicious_client: ['client5', 'client6', 'client7', 'client10', 'client11', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client28', 'client31', 'client36', 'client37', 'client38', 'client39', 'client42', 'client43', 'client44', 'client45', 'client46', 'client52', 'client53', 'client54', 'client65', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client79', 'client80', 'client81', 'client82', 'client87', 'client88', 'client89', 'client90', 'client91', 'client94', 'client95', 'client96', 'client99']
[INFO](2026/06/19/ 06:10:08 AM) [Round: 199] >> Number_malicious_client: 46
[INFO](2026/06/19/ 06:10:08 AM) [Round: 199] >> Server Defense accuracy: 0.260000
[INFO](2026/06/19/ 06:10:08 AM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/06/19/ 06:10:08 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/06/19/ 06:10:08 AM) [Round: 199] >> Time of aggregation: 0.405066 s
[INFO](2026/06/19/ 06:10:10 AM) [Round: 199] >> Global Model Test accuracy: 0.457910
[INFO](2026/06/19/ 06:10:10 AM) [Round: 199] >> Global Model Test loss: 0.858530


After a change in clients.py
RUN 4 : 

[INFO](2026/06/19/ 10:23:21 PM) agg_type: pca_agglomer_a
[INFO](2026/06/19/ 10:23:22 PM) [Round: 199] >> Detect_malicious_client: ['client5', 'client6', 'client7', 'client10', 'client11', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client28', 'client31', 'client36', 'client37', 'client38', 'client39', 'client42', 'client43', 'client44', 'client45', 'client46', 'client47', 'client51', 'client52', 'client53', 'client54', 'client59', 'client65', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client79', 'client80', 'client81', 'client82', 'client87', 'client88', 'client89', 'client90', 'client91', 'client94', 'client95', 'client96', 'client99']
[INFO](2026/06/19/ 10:23:22 PM) [Round: 199] >> Number_malicious_client: 49
[INFO](2026/06/19/ 10:23:22 PM) [Round: 199] >> Server Defense accuracy: 0.230000
[INFO](2026/06/19/ 10:23:22 PM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/06/19/ 10:23:22 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/06/19/ 10:23:22 PM) [Round: 199] >> Time of aggregation: 0.400185 s
[INFO](2026/06/19/ 10:23:23 PM) [Round: 199] >> Global Model Test accuracy: 0.936035
[INFO](2026/06/19/ 10:23:23 PM) [Round: 199] >> Global Model Test loss: 0.960239

RUN 5 : 

[INFO](2026/06/19/ 10:24:44 PM) agg_type: pca_agglomer_a
[INFO](2026/06/19/ 10:24:44 PM) [Round: 199] >> Detect_malicious_client: ['client5', 'client6', 'client7', 'client10', 'client11', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client28', 'client31', 'client36', 'client37', 'client38', 'client39', 'client42', 'client43', 'client44', 'client45', 'client46', 'client47', 'client51', 'client52', 'client53', 'client54', 'client59', 'client65', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client79', 'client80', 'client81', 'client82', 'client87', 'client88', 'client89', 'client90', 'client91', 'client94', 'client95', 'client96', 'client99']
[INFO](2026/06/19/ 10:24:44 PM) [Round: 199] >> Number_malicious_client: 49
[INFO](2026/06/19/ 10:24:44 PM) [Round: 199] >> Server Defense accuracy: 0.230000
[INFO](2026/06/19/ 10:24:44 PM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/06/19/ 10:24:44 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/06/19/ 10:24:44 PM) [Round: 199] >> Time of aggregation: 0.305984 s
[INFO](2026/06/19/ 10:24:46 PM) [Round: 199] >> Global Model Test accuracy: 0.937109
[INFO](2026/06/19/ 10:24:46 PM) [Round: 199] >> Global Model Test loss: 0.985600



python main.py --dataset mnist --byz_type GS_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10


RUN 1 : 

[INFO](2026/06/19/ 06:15:59 AM) agg_type: pca_agglomer_a
[INFO](2026/06/19/ 06:16:00 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/06/19/ 06:16:00 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/06/19/ 06:16:00 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/06/19/ 06:16:00 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/19/ 06:16:00 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/06/19/ 06:16:00 AM) [Round: 199] >> Time of aggregation: 0.270400 s
[INFO](2026/06/19/ 06:16:01 AM) [Round: 199] >> Global Model Test accuracy: 0.980664
[INFO](2026/06/19/ 06:16:01 AM) [Round: 199] >> Global Model Test loss: 0.086674

RUN 2 : 

[INFO](2026/06/19/ 09:03:25 AM) agg_type: pca_agglomer_a
[INFO](2026/06/19/ 09:03:26 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/06/19/ 09:03:26 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/06/19/ 09:03:26 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/06/19/ 09:03:26 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/19/ 09:03:26 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/06/19/ 09:03:26 AM) [Round: 199] >> Time of aggregation: 0.249213 s
[INFO](2026/06/19/ 09:03:26 AM) [Round: 199] >> Global Model Test accuracy: 0.981250
[INFO](2026/06/19/ 09:03:26 AM) [Round: 199] >> Global Model Test loss: 0.085357



python main.py --dataset mnist --byz_type LIT_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/06/20/ 12:09:27 AM) agg_type: pca_agglomer_a
[INFO](2026/06/20/ 12:09:27 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/06/20/ 12:09:27 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/06/20/ 12:09:27 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/06/20/ 12:09:27 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/20/ 12:09:27 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/06/20/ 12:09:27 AM) [Round: 199] >> Time of aggregation: 0.341022 s
[INFO](2026/06/20/ 12:09:30 AM) [Round: 199] >> Global ASR: 0.003800
[INFO](2026/06/20/ 12:09:30 AM) [Round: 199] >> Global Model Test accuracy: 0.979395
[INFO](2026/06/20/ 12:09:30 AM) [Round: 199] >> Global Model Test loss: 0.068852

RUN 2 : 

[INFO](2026/06/20/ 11:09:52 AM) agg_type: pca_agglomer_a
[INFO](2026/06/20/ 11:09:52 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/06/20/ 11:09:52 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/06/20/ 11:09:52 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/06/20/ 11:09:52 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/20/ 11:09:52 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/06/20/ 11:09:52 AM) [Round: 199] >> Time of aggregation: 0.260888 s
[INFO](2026/06/20/ 11:09:55 AM) [Round: 199] >> Global ASR: 0.003100
[INFO](2026/06/20/ 11:09:55 AM) [Round: 199] >> Global Model Test accuracy: 0.980078
[INFO](2026/06/20/ 11:09:55 AM) [Round: 199] >> Global Model Test loss: 0.070933



python main.py --dataset mnist --byz_type Scaling_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

RUN 1 : 

[INFO](2026/06/20/ 09:05:56 AM) agg_type: pca_agglomer_a
[INFO](2026/06/20/ 09:05:56 AM) [Round: 199] >> Detect_malicious_client: []
[INFO](2026/06/20/ 09:05:56 AM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/06/20/ 09:05:56 AM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/06/20/ 09:05:56 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/20/ 09:05:56 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/06/20/ 09:05:56 AM) [Round: 199] >> Time of aggregation: 0.421612 s
[INFO](2026/06/20/ 09:06:01 AM) [Round: 199] >> Global ASR: 0.901800
[INFO](2026/06/20/ 09:06:01 AM) [Round: 199] >> Global Model Test accuracy: 0.980664
[INFO](2026/06/20/ 09:06:01 AM) [Round: 199] >> Global Model Test loss: 0.091184

RUN 2 : 

[INFO](2026/06/20/ 09:08:02 AM) agg_type: pca_agglomer_a
[INFO](2026/06/20/ 09:08:02 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client4', 'client5', 'client6', 'client7', 'client8', 'client9', 'client10', 'client11', 'client12', 'client13', 'client14', 'client15', 'client16', 'client17', 'client18', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client26', 'client55', 'client57', 'client62', 'client63', 'client64', 'client67', 'client70', 'client72']
[INFO](2026/06/20/ 09:08:02 AM) [Round: 199] >> Number_malicious_client: 33
[INFO](2026/06/20/ 09:08:02 AM) [Round: 199] >> Server Defense accuracy: 0.670000
[INFO](2026/06/20/ 09:08:02 AM) [Round: 199] >> Server Detect malicious Precision: 0.424242
[INFO](2026/06/20/ 09:08:02 AM) [Round: 199] >> Server Detect malicious Recall: 0.500000
[INFO](2026/06/20/ 09:08:02 AM) [Round: 199] >> Time of aggregation: 0.332956 s
[INFO](2026/06/20/ 09:08:06 AM) [Round: 199] >> Global ASR: 0.902000
[INFO](2026/06/20/ 09:08:06 AM) [Round: 199] >> Global Model Test accuracy: 0.980371
[INFO](2026/06/20/ 09:08:06 AM) [Round: 199] >> Global Model Test loss: 0.089293

# here SGB not Adam
RUN 3 : 

[INFO](2026/06/20/ 08:14:50 PM) agg_type: pca_agglomer_a
[INFO](2026/06/20/ 08:14:50 PM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/06/20/ 08:14:50 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/06/20/ 08:14:50 PM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/06/20/ 08:14:50 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/20/ 08:14:50 PM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/06/20/ 08:14:50 PM) [Round: 199] >> Time of aggregation: 0.305572 s
[INFO](2026/06/20/ 08:14:55 PM) [Round: 199] >> Global ASR: 0.006900
[INFO](2026/06/20/ 08:14:55 PM) [Round: 199] >> Global Model Test accuracy: 0.911719
[INFO](2026/06/20/ 08:14:55 PM) [Round: 199] >> Global Model Test loss: 0.307682





# A partir de 20 00;49 juin, changed to SGB from Adam probe(optimizer)

# LF_ATTACK With SGB
python main.py --dataset mnist --byz_type LF_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10


[INFO](2026/06/20/ 09:35:04 AM) agg_type: pca_agglomer_a
[INFO](2026/06/20/ 09:35:04 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/06/20/ 09:35:04 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/06/20/ 09:35:04 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/06/20/ 09:35:04 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/20/ 09:35:04 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/06/20/ 09:35:04 AM) [Round: 199] >> Time of aggregation: 0.254614 s
[INFO](2026/06/20/ 09:35:05 AM) [Round: 199] >> Global Model Test accuracy: 0.912207
[INFO](2026/06/20/ 09:35:05 AM) [Round: 199] >> Global Model Test loss: 0.308700


python main.py --dataset mnist --byz_type no_attack --agg_type average --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/06/20/ 05:46:10 PM) agg_type: average
[INFO](2026/06/20/ 05:46:10 PM) [Round: 199] >> Detect_malicious_client: {}
[INFO](2026/06/20/ 05:46:10 PM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/06/20/ 05:46:10 PM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/06/20/ 05:46:10 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/20/ 05:46:10 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/06/20/ 05:46:10 PM) [Round: 199] >> Time of aggregation: 0.083121 s
[INFO](2026/06/20/ 05:46:11 PM) [Round: 199] >> Global Model Test accuracy: 0.913672
[INFO](2026/06/20/ 05:46:11 PM) [Round: 199] >> Global Model Test loss: 0.311547


# krum lf_attack
python main.py --dataset mnist --byz_type LF_attack --agg_type multi_krum --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/06/21/ 12:12:30 AM) agg_type: multi_krum
[INFO](2026/06/21/ 12:12:30 AM) [Round: 199] >> Detect_malicious_client: ['client74', 'client32', 'client12', 'client62', 'client40', 'client49', 'client8', 'client83', 'client29', 'client48', 'client72', 'client77', 'client57', 'client75', 'client2', 'client92', 'client17', 'client97', 'client26', 'client85', 'client60', 'client63', 'client34', 'client13', 'client55', 'client3', 'client15', 'client0']
[INFO](2026/06/21/ 12:12:30 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/06/21/ 12:12:30 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/06/21/ 12:12:30 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/21/ 12:12:30 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/06/21/ 12:12:30 AM) [Round: 199] >> Time of aggregation: 0.146006 s
[INFO](2026/06/21/ 12:12:31 AM) [Round: 199] >> Global Model Test accuracy: 0.909570
[INFO](2026/06/21/ 12:12:31 AM) [Round: 199] >> Global Model Test loss: 0.313471

# auror lf_attack

python main.py --dataset mnist --byz_type LF_attack --agg_type auror --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/06/21/ 12:12:38 AM) agg_type: auror
[INFO](2026/06/21/ 12:12:39 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/06/21/ 12:12:39 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/06/21/ 12:12:39 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/06/21/ 12:12:39 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/06/21/ 12:12:39 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/06/21/ 12:12:39 AM) [Round: 199] >> Time of aggregation: 0.237404 s
[INFO](2026/06/21/ 12:12:40 AM) [Round: 199] >> Global Model Test accuracy: 0.910156
[INFO](2026/06/21/ 12:12:40 AM) [Round: 199] >> Global Model Test loss: 0.311964

# 04 07

python main.py --dataset mnist --byz_type GS_attack --agg_type multi_krum --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/04/ 09:19:16 AM) agg_type: multi_krum
[INFO](2026/07/04/ 09:19:16 AM) [Round: 199] >> Detect_malicious_client: ['client17', 'client97', 'client26', 'client12', 'client0', 'client40', 'client92', 'client57', 'client48', 'client85', 'client2', 'client13', 'client77', 'client75', 'client72', 'client32', 'client55', 'client60', 'client63', 'client49', 'client29', 'client3', 'client83', 'client62', 'client15', 'client34', 'client8', 'client74']
[INFO](2026/07/04/ 09:19:16 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/04/ 09:19:16 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/04/ 09:19:16 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/04/ 09:19:16 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/04/ 09:19:16 AM) [Round: 199] >> Time of aggregation: 0.151789 s
[INFO](2026/07/04/ 09:19:18 AM) [Round: 199] >> Global Model Test accuracy: 0.911621
[INFO](2026/07/04/ 09:19:18 AM) [Round: 199] >> Global Model Test loss: 0.305906



python main.py --dataset mnist --byz_type GS_attack --agg_type auror --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/04/ 09:20:33 AM) agg_type: auror
[INFO](2026/07/04/ 09:20:34 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/04/ 09:20:34 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/04/ 09:20:34 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/04/ 09:20:34 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/04/ 09:20:34 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/04/ 09:20:34 AM) [Round: 199] >> Time of aggregation: 0.185905 s
[INFO](2026/07/04/ 09:20:34 AM) [Round: 199] >> Global Model Test accuracy: 0.911816
[INFO](2026/07/04/ 09:20:34 AM) [Round: 199] >> Global Model Test loss: 0.308876



python main.py --dataset mnist --byz_type GS_attack --agg_type foolsgold --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/04/ 09:20:07 AM) agg_type: foolsgold
[INFO](2026/07/04/ 09:20:07 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client1', 'client3', 'client4', 'client5', 'client6', 'client7', 'client8', 'client9', 'client10', 'client11', 'client12', 'client13', 'client14', 'client16', 'client17', 'client18', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client26', 'client28', 'client29', 'client30', 'client31', 'client35', 'client37', 'client38', 'client39', 'client41', 'client42', 'client44', 'client45', 'client47', 'client49', 'client50', 'client51', 'client52', 'client53', 'client54', 'client56', 'client58', 'client59', 'client61', 'client62', 'client63', 'client64', 'client65', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client73', 'client74', 'client75', 'client76', 'client77', 'client78', 'client79', 'client80', 'client81', 'client83', 'client84', 'client86', 'client87', 'client88', 'client89', 'client90', 'client91', 'client92', 'client93', 'client94', 'client95', 'client96', 'client98', 'client99']
[INFO](2026/07/04/ 09:20:07 AM) [Round: 199] >> Number_malicious_client: 82
[INFO](2026/07/04/ 09:20:07 AM) [Round: 199] >> Server Defense accuracy: 0.220000
[INFO](2026/07/04/ 09:20:07 AM) [Round: 199] >> Server Detect malicious Precision: 0.195122
[INFO](2026/07/04/ 09:20:07 AM) [Round: 199] >> Server Detect malicious Recall: 0.571429
[INFO](2026/07/04/ 09:20:07 AM) [Round: 199] >> Time of aggregation: 0.132560 s
[INFO](2026/07/04/ 09:20:08 AM) [Round: 199] >> Global Model Test accuracy: 0.096484
[INFO](2026/07/04/ 09:20:08 AM) [Round: 199] >> Global Model Test loss: 2.302575


python main.py --dataset mnist --byz_type Scaling_attack --agg_type multi_krum --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/04/ 07:35:44 PM) agg_type: multi_krum
[INFO](2026/07/04/ 07:35:44 PM) [Round: 199] >> Detect_malicious_client: ['client74', 'client2', 'client32', 'client49', 'client97', 'client48', 'client57', 'client77', 'client72', 'client29', 'client83', 'client12', 'client8', 'client75', 'client63', 'client62', 'client40', 'client34', 'client26', 'client17', 'client92', 'client55', 'client85', 'client3', 'client60', 'client15', 'client0', 'client13']
[INFO](2026/07/04/ 07:35:44 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/04/ 07:35:44 PM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/04/ 07:35:44 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/04/ 07:35:44 PM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/04/ 07:35:44 PM) [Round: 199] >> Time of aggregation: 0.126514 s
[INFO](2026/07/04/ 07:35:47 PM) [Round: 199] >> Global ASR: 0.007300
[INFO](2026/07/04/ 07:35:47 PM) [Round: 199] >> Global Model Test accuracy: 0.912891
[INFO](2026/07/04/ 07:35:47 PM) [Round: 199] >> Global Model Test loss: 0.304155


python main.py --dataset mnist --byz_type Scaling_attack --agg_type auror --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/04/ 07:33:49 PM) agg_type: auror
[INFO](2026/07/04/ 07:33:50 PM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/04/ 07:33:50 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/04/ 07:33:50 PM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/04/ 07:33:50 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/04/ 07:33:50 PM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/04/ 07:33:50 PM) [Round: 199] >> Time of aggregation: 0.238504 s
[INFO](2026/07/04/ 07:33:53 PM) [Round: 199] >> Global ASR: 0.006700
[INFO](2026/07/04/ 07:33:53 PM) [Round: 199] >> Global Model Test accuracy: 0.914844
[INFO](2026/07/04/ 07:33:53 PM) [Round: 199] >> Global Model Test loss: 0.307860



python main.py --dataset mnist --byz_type Scaling_attack --agg_type foolsgold --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/05/ 03:54:29 AM) agg_type: foolsgold
[INFO](2026/07/05/ 03:54:29 AM) [Round: 199] >> Detect_malicious_client: ['client1', 'client2', 'client3', 'client4', 'client5', 'client6', 'client7', 'client8', 'client9', 'client10', 'client11', 'client12', 'client13', 'client14', 'client15', 'client16', 'client17', 'client18', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client26', 'client27', 'client28', 'client29', 'client30', 'client31', 'client32', 'client33', 'client34', 'client35', 'client36', 'client37', 'client38', 'client39', 'client40', 'client41', 'client42', 'client43', 'client44', 'client45', 'client46', 'client47', 'client48', 'client49', 'client50', 'client51', 'client52', 'client53', 'client54', 'client56', 'client57', 'client58', 'client59', 'client60', 'client61', 'client62', 'client63', 'client64', 'client65', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client72', 'client73', 'client74', 'client75', 'client76', 'client77', 'client78', 'client79', 'client80', 'client81', 'client82', 'client83', 'client84', 'client85', 'client86', 'client87', 'client88', 'client89', 'client90', 'client91', 'client92', 'client93', 'client94', 'client95', 'client96', 'client97', 'client98', 'client99']
[INFO](2026/07/05/ 03:54:29 AM) [Round: 199] >> Number_malicious_client: 98
[INFO](2026/07/05/ 03:54:29 AM) [Round: 199] >> Server Defense accuracy: 0.260000
[INFO](2026/07/05/ 03:54:29 AM) [Round: 199] >> Server Detect malicious Precision: 0.265306
[INFO](2026/07/05/ 03:54:29 AM) [Round: 199] >> Server Detect malicious Recall: 0.928571
[INFO](2026/07/05/ 03:54:29 AM) [Round: 199] >> Time of aggregation: 0.191363 s
[INFO](2026/07/05/ 03:54:34 AM) [Round: 199] >> Global ASR: 0.898300
[INFO](2026/07/05/ 03:54:34 AM) [Round: 199] >> Global Model Test accuracy: 0.897070
[INFO](2026/07/05/ 03:54:34 AM) [Round: 199] >> Global Model Test loss: 0.357039


# clip_rate/2 

python main.py --dataset mnist --byz_type Scaling_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/05/ 10:46:52 AM) agg_type: pca_agglomer_a
[INFO](2026/07/05/ 10:46:53 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/05/ 10:46:53 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/05/ 10:46:53 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/05/ 10:46:53 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/05/ 10:46:53 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/05/ 10:46:53 AM) [Round: 199] >> Time of aggregation: 0.270471 s
[INFO](2026/07/05/ 10:46:56 AM) [Round: 199] >> Global ASR: 0.006600
[INFO](2026/07/05/ 10:46:56 AM) [Round: 199] >> Global Model Test accuracy: 0.912891
[INFO](2026/07/05/ 10:46:56 AM) [Round: 199] >> Global Model Test loss: 0.311154


# clip_rate without /2

python main.py --dataset mnist --byz_type Scaling_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/05/ 10:47:30 AM) agg_type: pca_agglomer_a
[INFO](2026/07/05/ 10:47:30 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/05/ 10:47:30 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/05/ 10:47:30 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/05/ 10:47:30 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/05/ 10:47:30 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/05/ 10:47:30 AM) [Round: 199] >> Time of aggregation: 0.216357 s
[INFO](2026/07/05/ 10:47:33 AM) [Round: 199] >> Global ASR: 0.006700
[INFO](2026/07/05/ 10:47:33 AM) [Round: 199] >> Global Model Test accuracy: 0.913574
[INFO](2026/07/05/ 10:47:33 AM) [Round: 199] >> Global Model Test loss: 0.305358



python main.py --dataset mnist --byz_type LF_attack --agg_type foolsgold --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/05/ 10:36:45 AM) agg_type: foolsgold
[INFO](2026/07/05/ 10:36:45 AM) [Round: 199] >> Detect_malicious_client: ['client1', 'client2', 'client3', 'client4', 'client5', 'client6', 'client7', 'client8', 'client9', 'client10', 'client11', 'client12', 'client14', 'client16', 'client17', 'client18', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client26', 'client27', 'client28', 'client29', 'client30', 'client31', 'client32', 'client33', 'client35', 'client37', 'client39', 'client40', 'client41', 'client42', 'client43', 'client44', 'client45', 'client47', 'client48', 'client49', 'client50', 'client51', 'client52', 'client53', 'client54', 'client56', 'client57', 'client58', 'client59', 'client60', 'client61', 'client62', 'client64', 'client65', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client72', 'client73', 'client74', 'client75', 'client76', 'client77', 'client78', 'client79', 'client80', 'client81', 'client82', 'client83', 'client84', 'client85', 'client87', 'client88', 'client89', 'client90', 'client91', 'client92', 'client93', 'client94', 'client95', 'client96', 'client97', 'client98', 'client99']
[INFO](2026/07/05/ 10:36:45 AM) [Round: 199] >> Number_malicious_client: 90
[INFO](2026/07/05/ 10:36:45 AM) [Round: 199] >> Server Defense accuracy: 0.260000
[INFO](2026/07/05/ 10:36:45 AM) [Round: 199] >> Server Detect malicious Precision: 0.244444
[INFO](2026/07/05/ 10:36:45 AM) [Round: 199] >> Server Detect malicious Recall: 0.785714
[INFO](2026/07/05/ 10:36:45 AM) [Round: 199] >> Time of aggregation: 0.144771 s
[INFO](2026/07/05/ 10:36:47 AM) [Round: 199] >> Global Model Test accuracy: 0.876270
[INFO](2026/07/05/ 10:36:47 AM) [Round: 199] >> Global Model Test loss: 1.181399





python main.py --dataset mnist --byz_type GS_attack   --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/05/ 08:18:46 PM) agg_type: pca_agglomer_a
[INFO](2026/07/05/ 08:18:47 PM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/05/ 08:18:47 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/05/ 08:18:47 PM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/05/ 08:18:47 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/05/ 08:18:47 PM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/05/ 08:18:47 PM) [Round: 199] >> Time of aggregation: 0.305598 s
[INFO](2026/07/05/ 08:18:48 PM) [Round: 199] >> Global Model Test accuracy: 0.914355
[INFO](2026/07/05/ 08:18:48 PM) [Round: 199] >> Global Model Test loss: 0.305022


python main.py --dataset mnist --byz_type LIT_attack  --agg_type auror --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/05/ 10:39:15 PM) agg_type: auror
[INFO](2026/07/05/ 10:39:15 PM) [Round: 199] >> Detect_malicious_client: ['client1', 'client9', 'client20', 'client21', 'client35', 'client45', 'client46', 'client68', 'client69', 'client87', 'client88']
[INFO](2026/07/05/ 10:39:15 PM) [Round: 199] >> Number_malicious_client: 11
[INFO](2026/07/05/ 10:39:15 PM) [Round: 199] >> Server Defense accuracy: 0.610000
[INFO](2026/07/05/ 10:39:15 PM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/07/05/ 10:39:15 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/07/05/ 10:39:15 PM) [Round: 199] >> Time of aggregation: 0.485921 s
[INFO](2026/07/05/ 10:39:20 PM) [Round: 199] >> Global ASR: 0.010300
[INFO](2026/07/05/ 10:39:20 PM) [Round: 199] >> Global Model Test accuracy: 0.914844
[INFO](2026/07/05/ 10:39:20 PM) [Round: 199] >> Global Model Test loss: 0.305923


python main.py --dataset mnist --byz_type LIT_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/06/ 06:56:43 AM) agg_type: pca_agglomer_a
[INFO](2026/07/06/ 06:56:43 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/06/ 06:56:43 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/06/ 06:56:43 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/06/ 06:56:43 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/06/ 06:56:43 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/06/ 06:56:43 AM) [Round: 199] >> Time of aggregation: 0.319667 s
[INFO](2026/07/06/ 06:56:46 AM) [Round: 199] >> Global ASR: 0.006500
[INFO](2026/07/06/ 06:56:46 AM) [Round: 199] >> Global Model Test accuracy: 0.912109
[INFO](2026/07/06/ 06:56:46 AM) [Round: 199] >> Global Model Test loss: 0.307075


python main.py --dataset mnist --byz_type LIT_attack --agg_type multi_krum --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/06/ 06:55:46 AM) agg_type: multi_krum
[INFO](2026/07/06/ 06:55:46 AM) [Round: 199] >> Detect_malicious_client: ['client67', 'client64', 'client52', 'client80', 'client47', 'client86', 'client58', 'client14', 'client96', 'client1', 'client43', 'client82', 'client45', 'client94', 'client5', 'client28', 'client99', 'client35', 'client41', 'client6', 'client87', 'client71', 'client21', 'client59', 'client36', 'client42', 'client38', 'client46']
[INFO](2026/07/06/ 06:55:46 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/06/ 06:55:46 AM) [Round: 199] >> Server Defense accuracy: 0.440000
[INFO](2026/07/06/ 06:55:46 AM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/07/06/ 06:55:46 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/07/06/ 06:55:46 AM) [Round: 199] >> Time of aggregation: 0.162173 s
[INFO](2026/07/06/ 06:55:50 AM) [Round: 199] >> Global ASR: 0.012500
[INFO](2026/07/06/ 06:55:50 AM) [Round: 199] >> Global Model Test accuracy: 0.912891
[INFO](2026/07/06/ 06:55:50 AM) [Round: 199] >> Global Model Test loss: 0.309093


python main.py --dataset mnist --byz_type LIT_attack --agg_type foolsgold --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/06/ 09:17:23 AM) agg_type: foolsgold
[INFO](2026/07/06/ 09:17:23 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client7', 'client8', 'client9', 'client11', 'client12', 'client13', 'client15', 'client17', 'client22', 'client24', 'client25', 'client26', 'client27', 'client29', 'client30', 'client32', 'client33', 'client34', 'client37', 'client38', 'client39', 'client40', 'client42', 'client44', 'client48', 'client49', 'client51', 'client54', 'client55', 'client56', 'client57', 'client60', 'client61', 'client62', 'client63', 'client64', 'client65', 'client68', 'client70', 'client72', 'client73', 'client74', 'client75', 'client76', 'client77', 'client78', 'client80', 'client81', 'client83', 'client84', 'client85', 'client88', 'client89', 'client91', 'client92', 'client93', 'client95', 'client96', 'client97', 'client98']
[INFO](2026/07/06/ 09:17:23 AM) [Round: 199] >> Number_malicious_client: 63
[INFO](2026/07/06/ 09:17:23 AM) [Round: 199] >> Server Defense accuracy: 0.650000
[INFO](2026/07/06/ 09:17:23 AM) [Round: 199] >> Server Detect malicious Precision: 0.444444
[INFO](2026/07/06/ 09:17:23 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/06/ 09:17:23 AM) [Round: 199] >> Time of aggregation: 0.132498 s
[INFO](2026/07/06/ 09:17:26 AM) [Round: 199] >> Global ASR: 0.006900
[INFO](2026/07/06/ 09:17:26 AM) [Round: 199] >> Global Model Test accuracy: 0.911426
[INFO](2026/07/06/ 09:17:26 AM) [Round: 199] >> Global Model Test loss: 0.311253



python main.py --dataset mnist --byz_type LF_attack       --agg_type average --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/06/ 10:08:28 PM) agg_type: average
[INFO](2026/07/06/ 10:08:28 PM) [Round: 199] >> Detect_malicious_client: {}
[INFO](2026/07/06/ 10:08:28 PM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/07/06/ 10:08:28 PM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/07/06/ 10:08:28 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/06/ 10:08:28 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/07/06/ 10:08:28 PM) [Round: 199] >> Time of aggregation: 0.149858 s
[INFO](2026/07/06/ 10:08:29 PM) [Round: 199] >> Global Model Test accuracy: 0.908984
[INFO](2026/07/06/ 10:08:29 PM) [Round: 199] >> Global Model Test loss: 0.682272


python main.py --dataset mnist --byz_type GS_attack       --agg_type average --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/06/ 10:08:47 PM) agg_type: average
[INFO](2026/07/06/ 10:08:47 PM) [Round: 199] >> Detect_malicious_client: {}
[INFO](2026/07/06/ 10:08:47 PM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/07/06/ 10:08:47 PM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/07/06/ 10:08:47 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/06/ 10:08:47 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/07/06/ 10:08:47 PM) [Round: 199] >> Time of aggregation: 0.086759 s
[INFO](2026/07/06/ 10:08:48 PM) [Round: 199] >> Global Model Test accuracy: 0.113770
[INFO](2026/07/06/ 10:08:48 PM) [Round: 199] >> Global Model Test loss: 2.302547


python main.py --dataset mnist --byz_type LIT_attack      --agg_type average --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/07/ 12:38:04 AM) agg_type: average
[INFO](2026/07/07/ 12:38:04 AM) [Round: 199] >> Detect_malicious_client: {}
[INFO](2026/07/07/ 12:38:04 AM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/07/07/ 12:38:04 AM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/07/07/ 12:38:04 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/07/ 12:38:04 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/07/07/ 12:38:04 AM) [Round: 199] >> Time of aggregation: 0.125111 s
[INFO](2026/07/07/ 12:38:08 AM) [Round: 199] >> Global ASR: 0.010200
[INFO](2026/07/07/ 12:38:08 AM) [Round: 199] >> Global Model Test accuracy: 0.913965
[INFO](2026/07/07/ 12:38:08 AM) [Round: 199] >> Global Model Test loss: 0.304897


python main.py --dataset mnist --byz_type Scaling_attack  --agg_type average --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/07/ 06:16:57 AM) agg_type: average
[INFO](2026/07/07/ 06:16:57 AM) [Round: 199] >> Detect_malicious_client: {}
[INFO](2026/07/07/ 06:16:57 AM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/07/07/ 06:16:57 AM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/07/07/ 06:16:57 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/07/ 06:16:57 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/07/07/ 06:16:57 AM) [Round: 199] >> Time of aggregation: 0.140601 s
[INFO](2026/07/07/ 06:17:02 AM) [Round: 199] >> Global ASR: 0.899200
[INFO](2026/07/07/ 06:17:02 AM) [Round: 199] >> Global Model Test accuracy: 0.909961
[INFO](2026/07/07/ 06:17:02 AM) [Round: 199] >> Global Model Test loss: 0.324779


# run 2
python main.py --dataset mnist --byz_type LIT_attack --agg_type multi_krum --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/07/ 08:39:29 AM) agg_type: multi_krum
[INFO](2026/07/07/ 08:39:29 AM) [Round: 199] >> Detect_malicious_client: ['client79', 'client99', 'client37', 'client35', 'client10', 'client66', 'client4', 'client20', 'client58', 'client80', 'client52', 'client43', 'client19', 'client67', 'client1', 'client82', 'client5', 'client45', 'client87', 'client14', 'client59', 'client6', 'client41', 'client36', 'client71', 'client38', 'client86', 'client21']
[INFO](2026/07/07/ 08:39:29 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/07/ 08:39:29 AM) [Round: 199] >> Server Defense accuracy: 0.440000
[INFO](2026/07/07/ 08:39:29 AM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/07/07/ 08:39:29 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/07/07/ 08:39:29 AM) [Round: 199] >> Time of aggregation: 0.143864 s
[INFO](2026/07/07/ 08:39:33 AM) [Round: 199] >> Global ASR: 0.011400
[INFO](2026/07/07/ 08:39:33 AM) [Round: 199] >> Global Model Test accuracy: 0.913672
[INFO](2026/07/07/ 08:39:33 AM) [Round: 199] >> Global Model Test loss: 0.308451


python main.py --dataset mnist --byz_type GS_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/07/ 09:15:36 AM) agg_type: pca_agglomer_a
[INFO](2026/07/07/ 09:15:37 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/07/ 09:15:37 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/07/ 09:15:37 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/07/ 09:15:37 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/07/ 09:15:37 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/07/ 09:15:37 AM) [Round: 199] >> Time of aggregation: 0.256424 s
[INFO](2026/07/07/ 09:15:38 AM) [Round: 199] >> Global Model Test accuracy: 0.912598
[INFO](2026/07/07/ 09:15:38 AM) [Round: 199] >> Global Model Test loss: 0.307460


# run 2
python main.py --dataset mnist --byz_type Scaling_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/07/ 11:10:20 AM) agg_type: pca_agglomer_a
[INFO](2026/07/07/ 11:10:20 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/07/ 11:10:20 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/07/ 11:10:20 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/07/ 11:10:20 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/07/ 11:10:20 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/07/ 11:10:20 AM) [Round: 199] >> Time of aggregation: 0.208666 s
[INFO](2026/07/07/ 11:10:23 AM) [Round: 199] >> Global ASR: 0.007500
[INFO](2026/07/07/ 11:10:23 AM) [Round: 199] >> Global Model Test accuracy: 0.911914
[INFO](2026/07/07/ 11:10:23 AM) [Round: 199] >> Global Model Test loss: 0.306953


python main.py --dataset mnist --byz_type Scaling_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/07/ 08:41:43 PM) agg_type: pca_agglomer_a
[INFO](2026/07/07/ 08:41:44 PM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/07/ 08:41:44 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/07/ 08:41:44 PM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/07/ 08:41:44 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/07/ 08:41:44 PM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/07/ 08:41:44 PM) [Round: 199] >> Time of aggregation: 0.332868 s
[INFO](2026/07/07/ 08:41:48 PM) [Round: 199] >> Global ASR: 0.007000
[INFO](2026/07/07/ 08:41:48 PM) [Round: 199] >> Global Model Test accuracy: 0.911426
[INFO](2026/07/07/ 08:41:48 PM) [Round: 199] >> Global Model Test loss: 0.308635


python main.py --dataset mnist --byz_type GS_attack --agg_type multi_krum --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/07/ 09:23:28 PM) agg_type: multi_krum
[INFO](2026/07/07/ 09:23:28 PM) [Round: 199] >> Detect_malicious_client: ['client49', 'client57', 'client8', 'client92', 'client55', 'client32', 'client34', 'client12', 'client77', 'client40', 'client29', 'client72', 'client26', 'client74', 'client17', 'client83', 'client0', 'client60', 'client97', 'client48', 'client13', 'client15', 'client75', 'client3', 'client85', 'client2', 'client63', 'client62']
[INFO](2026/07/07/ 09:23:28 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/07/ 09:23:28 PM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/07/ 09:23:28 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/07/ 09:23:28 PM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/07/ 09:23:28 PM) [Round: 199] >> Time of aggregation: 0.119557 s
[INFO](2026/07/07/ 09:23:29 PM) [Round: 199] >> Global Model Test accuracy: 0.908398
[INFO](2026/07/07/ 09:23:29 PM) [Round: 199] >> Global Model Test loss: 0.311767


python main.py --dataset mnist --byz_type GS_attack --agg_type auror --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/07/ 09:25:03 PM) agg_type: auror
[INFO](2026/07/07/ 09:25:03 PM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/07/ 09:25:03 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/07/ 09:25:03 PM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/07/ 09:25:03 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/07/ 09:25:03 PM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/07/ 09:25:03 PM) [Round: 199] >> Time of aggregation: 0.209602 s
[INFO](2026/07/07/ 09:25:04 PM) [Round: 199] >> Global Model Test accuracy: 0.911621
[INFO](2026/07/07/ 09:25:04 PM) [Round: 199] >> Global Model Test loss: 0.307133



python main.py --dataset mnist --byz_type GS_attack --agg_type foolsgold --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/08/ 05:21:14 AM) agg_type: foolsgold
[INFO](2026/07/08/ 05:21:14 AM) [Round: 199] >> Detect_malicious_client: ['client1', 'client2', 'client3', 'client5', 'client7', 'client8', 'client9', 'client10', 'client11', 'client12', 'client13', 'client14', 'client16', 'client17', 'client18', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client26', 'client28', 'client30', 'client31', 'client32', 'client33', 'client37', 'client39', 'client40', 'client41', 'client42', 'client44', 'client45', 'client47', 'client49', 'client50', 'client51', 'client52', 'client53', 'client54', 'client56', 'client58', 'client59', 'client61', 'client62', 'client63', 'client64', 'client65', 'client66', 'client67', 'client69', 'client70', 'client71', 'client72', 'client73', 'client75', 'client76', 'client78', 'client79', 'client80', 'client81', 'client84', 'client87', 'client88', 'client89', 'client90', 'client91', 'client92', 'client93', 'client94', 'client95', 'client96', 'client97', 'client98', 'client99']
[INFO](2026/07/08/ 05:21:14 AM) [Round: 199] >> Number_malicious_client: 77
[INFO](2026/07/08/ 05:21:14 AM) [Round: 199] >> Server Defense accuracy: 0.270000
[INFO](2026/07/08/ 05:21:14 AM) [Round: 199] >> Server Detect malicious Precision: 0.207792
[INFO](2026/07/08/ 05:21:14 AM) [Round: 199] >> Server Detect malicious Recall: 0.571429
[INFO](2026/07/08/ 05:21:14 AM) [Round: 199] >> Time of aggregation: 0.171481 s
[INFO](2026/07/08/ 05:21:15 AM) [Round: 199] >> Global Model Test accuracy: 0.096484
[INFO](2026/07/08/ 05:21:15 AM) [Round: 199] >> Global Model Test loss: 2.302590


python main.py --dataset mnist --byz_type Scaling_attack --agg_type multi_krum --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/08/ 05:35:12 AM) agg_type: multi_krum
[INFO](2026/07/08/ 05:35:12 AM) [Round: 199] >> Detect_malicious_client: ['client74', 'client57', 'client48', 'client32', 'client49', 'client75', 'client97', 'client92', 'client72', 'client12', 'client29', 'client8', 'client62', 'client77', 'client83', 'client2', 'client85', 'client26', 'client40', 'client15', 'client63', 'client55', 'client34', 'client3', 'client17', 'client13', 'client60', 'client0']
[INFO](2026/07/08/ 05:35:12 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/08/ 05:35:12 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/08/ 05:35:12 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/08/ 05:35:12 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/08/ 05:35:12 AM) [Round: 199] >> Time of aggregation: 0.145402 s
[INFO](2026/07/08/ 05:35:17 AM) [Round: 199] >> Global ASR: 0.006800
[INFO](2026/07/08/ 05:35:17 AM) [Round: 199] >> Global Model Test accuracy: 0.912109
[INFO](2026/07/08/ 05:35:17 AM) [Round: 199] >> Global Model Test loss: 0.308368


python main.py --dataset mnist --byz_type Scaling_attack --agg_type auror --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/08/ 05:51:44 AM) agg_type: auror
[INFO](2026/07/08/ 05:51:44 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/08/ 05:51:44 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/08/ 05:51:44 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/08/ 05:51:44 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/08/ 05:51:44 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/08/ 05:51:44 AM) [Round: 199] >> Time of aggregation: 0.195995 s
[INFO](2026/07/08/ 05:51:48 AM) [Round: 199] >> Global ASR: 0.007000
[INFO](2026/07/08/ 05:51:48 AM) [Round: 199] >> Global Model Test accuracy: 0.911816
[INFO](2026/07/08/ 05:51:48 AM) [Round: 199] >> Global Model Test loss: 0.309001


python main.py --dataset mnist --byz_type Scaling_attack --agg_type foolsgold --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/08/ 08:21:53 AM) agg_type: foolsgold
[INFO](2026/07/08/ 08:21:53 AM) [Round: 199] >> Detect_malicious_client: ['client1', 'client2', 'client3', 'client4', 'client5', 'client6', 'client7', 'client8', 'client9', 'client10', 'client11', 'client12', 'client14', 'client16', 'client17', 'client18', 'client19', 'client20', 'client21', 'client22', 'client23', 'client24', 'client25', 'client26', 'client27', 'client28', 'client29', 'client30', 'client31', 'client32', 'client33', 'client34', 'client35', 'client36', 'client37', 'client38', 'client39', 'client41', 'client42', 'client43', 'client44', 'client45', 'client46', 'client47', 'client48', 'client49', 'client50', 'client51', 'client52', 'client53', 'client54', 'client55', 'client56', 'client57', 'client58', 'client59', 'client60', 'client61', 'client62', 'client63', 'client64', 'client65', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client72', 'client73', 'client74', 'client75', 'client76', 'client77', 'client78', 'client79', 'client80', 'client81', 'client82', 'client83', 'client84', 'client85', 'client86', 'client87', 'client88', 'client89', 'client90', 'client91', 'client92', 'client93', 'client94', 'client95', 'client96', 'client97', 'client98', 'client99']
[INFO](2026/07/08/ 08:21:53 AM) [Round: 199] >> Number_malicious_client: 96
[INFO](2026/07/08/ 08:21:53 AM) [Round: 199] >> Server Defense accuracy: 0.240000
[INFO](2026/07/08/ 08:21:53 AM) [Round: 199] >> Server Detect malicious Precision: 0.250000
[INFO](2026/07/08/ 08:21:53 AM) [Round: 199] >> Server Detect malicious Recall: 0.857143
[INFO](2026/07/08/ 08:21:53 AM) [Round: 199] >> Time of aggregation: 0.106422 s
[INFO](2026/07/08/ 08:21:56 AM) [Round: 199] >> Global ASR: 0.901700
[INFO](2026/07/08/ 08:21:56 AM) [Round: 199] >> Global Model Test accuracy: 0.906055
[INFO](2026/07/08/ 08:21:56 AM) [Round: 199] >> Global Model Test loss: 0.339369




python main.py --dataset mnist --byz_type LF_attack --agg_type average --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/08/ 10:52:58 PM) agg_type: average
[INFO](2026/07/08/ 10:52:58 PM) [Round: 199] >> Detect_malicious_client: {}
[INFO](2026/07/08/ 10:52:58 PM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/07/08/ 10:52:58 PM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/07/08/ 10:52:58 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/08/ 10:52:58 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/07/08/ 10:52:58 PM) [Round: 199] >> Time of aggregation: 0.066656 s
[INFO](2026/07/08/ 10:52:59 PM) [Round: 199] >> Global Model Test accuracy: 0.907422
[INFO](2026/07/08/ 10:52:59 PM) [Round: 199] >> Global Model Test loss: 0.685475


python main.py --dataset mnist --byz_type LF_attack --agg_type average --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/08/ 10:52:49 PM) agg_type: average
[INFO](2026/07/08/ 10:52:49 PM) [Round: 199] >> Detect_malicious_client: {}
[INFO](2026/07/08/ 10:52:49 PM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/07/08/ 10:52:49 PM) [Round: 199] >> Server Defense accuracy: 0.720000
[INFO](2026/07/08/ 10:52:49 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/08/ 10:52:49 PM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/07/08/ 10:52:49 PM) [Round: 199] >> Time of aggregation: 0.069905 s
[INFO](2026/07/08/ 10:52:50 PM) [Round: 199] >> Global Model Test accuracy: 0.911035
[INFO](2026/07/08/ 10:52:50 PM) [Round: 199] >> Global Model Test loss: 0.677525



python main.py --dataset mnist --byz_type LF_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/09/ 08:17:36 AM) agg_type: pca_agglomer_a
[INFO](2026/07/09/ 08:17:37 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/09/ 08:17:37 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/09/ 08:17:37 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/09/ 08:17:37 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/09/ 08:17:37 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/09/ 08:17:37 AM) [Round: 199] >> Time of aggregation: 0.221452 s
[INFO](2026/07/09/ 08:17:38 AM) [Round: 199] >> Global Model Test accuracy: 0.914062
[INFO](2026/07/09/ 08:17:38 AM) [Round: 199] >> Global Model Test loss: 0.307269



python main.py --dataset mnist --byz_type LF_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/09/ 08:16:41 AM) agg_type: pca_agglomer_a
[INFO](2026/07/09/ 08:16:42 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/09/ 08:16:42 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/09/ 08:16:42 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/09/ 08:16:42 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/09/ 08:16:42 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/09/ 08:16:42 AM) [Round: 199] >> Time of aggregation: 0.299460 s
[INFO](2026/07/09/ 08:16:43 AM) [Round: 199] >> Global Model Test accuracy: 0.912402
[INFO](2026/07/09/ 08:16:43 AM) [Round: 199] >> Global Model Test loss: 0.309759


python main.py --dataset mnist --byz_type LIT_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/09/ 09:51:11 AM) agg_type: pca_agglomer_a
[INFO](2026/07/09/ 09:51:11 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/09/ 09:51:11 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/09/ 09:51:11 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/09/ 09:51:11 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/09/ 09:51:11 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/09/ 09:51:11 AM) [Round: 199] >> Time of aggregation: 0.220364 s
[INFO](2026/07/09/ 09:51:14 AM) [Round: 199] >> Global ASR: 0.007100
[INFO](2026/07/09/ 09:51:14 AM) [Round: 199] >> Global Model Test accuracy: 0.914453
[INFO](2026/07/09/ 09:51:14 AM) [Round: 199] >> Global Model Test loss: 0.303493

## to results
python main.py --dataset mnist --byz_type LF_attack --agg_type pca_agglomer_a --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/10/ 03:56:35 AM) agg_type: pca_agglomer_a
[INFO](2026/07/10/ 03:56:36 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/10/ 03:56:36 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/10/ 03:56:36 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/10/ 03:56:36 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/10/ 03:56:36 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/10/ 03:56:36 AM) [Round: 199] >> Time of aggregation: 0.282450 s
[INFO](2026/07/10/ 03:56:37 AM) [Round: 199] >> Global Model Test accuracy: 0.913574
[INFO](2026/07/10/ 03:56:37 AM) [Round: 199] >> Global Model Test loss: 0.305754



# ADAM
python main.py --dataset mnist --byz_type no_attack --agg_type average --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10 

[INFO](2026/07/10/ 01:47:24 AM) agg_type: average
[INFO](2026/07/10/ 01:47:24 AM) [Round: 199] >> Detect_malicious_client: {}
[INFO](2026/07/10/ 01:47:24 AM) [Round: 199] >> Number_malicious_client: 0
[INFO](2026/07/10/ 01:47:24 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/10/ 01:47:24 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/10/ 01:47:24 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/07/10/ 01:47:24 AM) [Round: 199] >> Time of aggregation: 0.060343 s
[INFO](2026/07/10/ 01:47:25 AM) [Round: 199] >> Global Model Test accuracy: 0.978516
[INFO](2026/07/10/ 01:47:25 AM) [Round: 199] >> Global Model Test loss: 0.101759


# back to sgd
python main.py --dataset mnist --byz_type LIT_attack --agg_type auror --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10


[INFO](2026/07/10/ 06:12:14 AM) agg_type: auror
[INFO](2026/07/10/ 06:12:15 AM) [Round: 199] >> Detect_malicious_client: ['client5', 'client14', 'client22', 'client25', 'client37', 'client38', 'client42', 'client59', 'client66', 'client71', 'client86']
[INFO](2026/07/10/ 06:12:15 AM) [Round: 199] >> Number_malicious_client: 11
[INFO](2026/07/10/ 06:12:15 AM) [Round: 199] >> Server Defense accuracy: 0.610000
[INFO](2026/07/10/ 06:12:15 AM) [Round: 199] >> Server Detect malicious Precision: 0.000000
[INFO](2026/07/10/ 06:12:15 AM) [Round: 199] >> Server Detect malicious Recall: 0.000000
[INFO](2026/07/10/ 06:12:15 AM) [Round: 199] >> Time of aggregation: 0.278428 s
[INFO](2026/07/10/ 06:12:19 AM) [Round: 199] >> Global ASR: 0.010000
[INFO](2026/07/10/ 06:12:19 AM) [Round: 199] >> Global Model Test accuracy: 0.912598
[INFO](2026/07/10/ 06:12:19 AM) [Round: 199] >> Global Model Test loss: 0.309978


python main.py --dataset mnist --byz_type LIT_attack --agg_type foolsgold --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/10/ 06:12:45 AM) agg_type: foolsgold
[INFO](2026/07/10/ 06:12:46 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client1', 'client2', 'client3', 'client4', 'client5', 'client6', 'client7', 'client8', 'client9', 'client10', 'client11', 'client12', 'client13', 'client15', 'client16', 'client17', 'client18', 'client19', 'client22', 'client23', 'client24', 'client25', 'client26', 'client27', 'client29', 'client30', 'client31', 'client32', 'client33', 'client34', 'client35', 'client37', 'client39', 'client40', 'client41', 'client42', 'client43', 'client44', 'client45', 'client46', 'client47', 'client48', 'client49', 'client50', 'client51', 'client52', 'client53', 'client54', 'client55', 'client56', 'client57', 'client59', 'client60', 'client61', 'client62', 'client63', 'client64', 'client65', 'client66', 'client67', 'client68', 'client69', 'client70', 'client71', 'client72', 'client73', 'client74', 'client75', 'client76', 'client77', 'client78', 'client79', 'client80', 'client81', 'client82', 'client83', 'client84', 'client85', 'client86', 'client87', 'client88', 'client89', 'client90', 'client91', 'client92', 'client93', 'client94', 'client95', 'client97', 'client98', 'client99']
[INFO](2026/07/10/ 06:12:46 AM) [Round: 199] >> Number_malicious_client: 92
[INFO](2026/07/10/ 06:12:46 AM) [Round: 199] >> Server Defense accuracy: 0.360000
[INFO](2026/07/10/ 06:12:46 AM) [Round: 199] >> Server Detect malicious Precision: 0.304348
[INFO](2026/07/10/ 06:12:46 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/10/ 06:12:46 AM) [Round: 199] >> Time of aggregation: 0.120687 s
[INFO](2026/07/10/ 06:12:48 AM) [Round: 199] >> Global ASR: 0.006600
[INFO](2026/07/10/ 06:12:48 AM) [Round: 199] >> Global Model Test accuracy: 0.912793
[INFO](2026/07/10/ 06:12:48 AM) [Round: 199] >> Global Model Test loss: 0.311319

# ADAM run to verify previous results
python main.py --dataset mnist --byz_type GS_attack --agg_type pca_hdbscan_b --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/11/ 09:12:18 PM) agg_type: pca_hdbscan_b
[INFO](2026/07/11/ 09:12:19 PM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/11/ 09:12:19 PM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/11/ 09:12:19 PM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/11/ 09:12:19 PM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/11/ 09:12:19 PM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/11/ 09:12:19 PM) [Round: 199] >> Time of aggregation: 0.245852 s
[INFO](2026/07/11/ 09:12:19 PM) [Round: 199] >> Global Model Test accuracy: 0.981250
[INFO](2026/07/11/ 09:12:19 PM) [Round: 199] >> Global Model Test loss: 0.082598


python main.py --dataset mnist --byz_type LF_attack --agg_type pca_hdbscan_b --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/12/ 03:58:13 AM) agg_type: pca_hdbscan_b
[INFO](2026/07/12/ 03:58:14 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client8', 'client12', 'client13', 'client15', 'client17', 'client26', 'client29', 'client32', 'client34', 'client40', 'client48', 'client49', 'client55', 'client57', 'client60', 'client62', 'client63', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client92', 'client97']
[INFO](2026/07/12/ 03:58:14 AM) [Round: 199] >> Number_malicious_client: 28
[INFO](2026/07/12/ 03:58:14 AM) [Round: 199] >> Server Defense accuracy: 1.000000
[INFO](2026/07/12/ 03:58:14 AM) [Round: 199] >> Server Detect malicious Precision: 1.000000
[INFO](2026/07/12/ 03:58:14 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/12/ 03:58:14 AM) [Round: 199] >> Time of aggregation: 0.263832 s
[INFO](2026/07/12/ 03:58:15 AM) [Round: 199] >> Global Model Test accuracy: 0.911035
[INFO](2026/07/12/ 03:58:15 AM) [Round: 199] >> Global Model Test loss: 0.307850



python main.py --dataset mnist --byz_type LIT_attack --agg_type pca_hdbscan_b --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10

[INFO](2026/07/12/ 05:33:40 AM) agg_type: pca_hdbscan_b
[INFO](2026/07/12/ 05:33:40 AM) [Round: 199] >> Detect_malicious_client: ['client0', 'client2', 'client3', 'client6', 'client8', 'client12', 'client13', 'client15', 'client17', 'client20', 'client21', 'client26', 'client28', 'client29', 'client32', 'client34', 'client36', 'client38', 'client40', 'client41', 'client46', 'client48', 'client49', 'client55', 'client57', 'client59', 'client60', 'client62', 'client63', 'client71', 'client72', 'client74', 'client75', 'client77', 'client83', 'client85', 'client86', 'client92', 'client97']
[INFO](2026/07/12/ 05:33:40 AM) [Round: 199] >> Number_malicious_client: 39
[INFO](2026/07/12/ 05:33:40 AM) [Round: 199] >> Server Defense accuracy: 0.890000
[INFO](2026/07/12/ 05:33:40 AM) [Round: 199] >> Server Detect malicious Precision: 0.717949
[INFO](2026/07/12/ 05:33:40 AM) [Round: 199] >> Server Detect malicious Recall: 1.000000
[INFO](2026/07/12/ 05:33:40 AM) [Round: 199] >> Time of aggregation: 0.199655 s
[INFO](2026/07/12/ 05:33:43 AM) [Round: 199] >> Global ASR: 0.006200
[INFO](2026/07/12/ 05:33:43 AM) [Round: 199] >> Global Model Test accuracy: 0.912305
[INFO](2026/07/12/ 05:33:43 AM) [Round: 199] >> Global Model Test loss: 0.308322
