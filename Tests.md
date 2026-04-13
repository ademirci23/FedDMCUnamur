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



Valeur dans la table 4 FEDDMC : 8.81, dans le test : 55-60 average
-> Grosse différence, car j'ai lancé avec IID = TRUE, dans la papier, c'est indiqué q'ils lancent avec IID = false.
Test 3 redone with : 
python main.py --dataset mnist --byz_type LIT_attack --agg_type multi_krum --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01 --pca_d 10


Test 4 : 
python main.py --dataset mnist --byz_type LIT_attack --agg_type auror --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01
Résultat attendu (Table IV du paper, moyenne sur 5 runs) :
TACC ≈ 98.07%
ASR ≈ 5.75%
- Results : 


Test 5 : 
python main.py --dataset mnist --byz_type LIT_attack --agg_type foolsgold --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 --learning_rate 0.01
Résultat attendu (Table IV) :
TACC ≈ 98.00%
ASR ≈ 41.59%