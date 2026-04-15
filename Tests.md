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

