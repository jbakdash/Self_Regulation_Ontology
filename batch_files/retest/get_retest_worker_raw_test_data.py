import pandas as pd
data = pd.read_pickle('/oak/stanford/groups/russpold/users/ieisenbe/uh2/behavioral_data/mturk_complete_data_post.pkl')
retest_workers = ['s198', 's409', 's473', 's286', 's017', 's092', 's403', 's103','s081', 's357', 's291', 's492', 's294', 's145', 's187', 's226','s368', 's425', 's094', 's430', 's376', 's284', 's421', 's034','s233', 's027', 's108', 's089', 's196', 's066', 's374', 's007','s509', 's365', 's305', 's453', 's504', 's161', 's441', 's205','s112', 's218', 's129', 's093', 's180', 's128', 's170', 's510','s502', 's477', 's551', 's307', 's556', 's121', 's237', 's481','s259', 's467', 's163', 's111', 's427', 's508', 's190', 's091','s207', 's484', 's449', 's049', 's336', 's212', 's142', 's313','s369', 's165', 's028', 's216', 's346', 's083', 's391', 's388','s384', 's275', 's442', 's505', 's098', 's456', 's209', 's372','s179', 's168', 's084', 's329', 's373', 's065', 's277', 's026','s011', 's063', 's507', 's005', 's495', 's501', 's032', 's326','s396', 's420', 's469', 's244', 's359', 's110', 's383', 's254','s060', 's339', 's380', 's471', 's206', 's182', 's500', 's314','s285', 's086', 's012', 's097', 's149', 's192', 's173', 's262','s273', 's402', 's015', 's014', 's085', 's489', 's071', 's062','s042', 's009', 's408', 's184', 's106', 's397', 's451', 's269','s295', 's265', 's301', 's082', 's238', 's328', 's334']
retest_subs_test_data_post = data[data['worker_id'].isin(retest_workers)]
retest_subs_test_data_post = retest_subs_test_data_post.reset_index()
retest_subs_test_data_post.to_pickle('/oak/stanford/groups/russpold/users/ieisenbe/uh2/behavioral_data/retest_subs_test_data_post.pkl')