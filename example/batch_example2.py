print("example")
mount_dir = "/root/data_ws/"
f = open(mount_dir+"test_batch.txt", "a")
f.write("This is testing file for batch job")
f.close()