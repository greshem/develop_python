args = ["/usr/bin/mkisofs",
                "-J", "-r",
                "-hide-rr-moved", "-hide-joliet-trans-tbl",
                "-V", "self.fslabel",
                "-o", "iso"];
print args
