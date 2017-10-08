
def get_sector_size():
    try:
        with open(b"/sys/block/sda/queue/hw_sector_size") as f:
            return int(f.read())
    except (IOError, ValueError):
        # man iostat states that sectors are equivalent with blocks and
        # have a size of 512 bytes since 2.4 kernels. This value is
        # needed to calculate the amount of disk I/O in bytes.
        return 512

if __name__=="__main__":
    print get_sector_size();
