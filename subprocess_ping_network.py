def test_network():
    import os
    import subprocess
     
    fnull = open(os.devnull, 'w')
    return1 = subprocess.call('ping 8.8.8.8', shell = True, stdout = fnull, stderr = fnull)
    fnull.close()
    if return1:
      return False
    else:
      getip()
      return True

test_network();
