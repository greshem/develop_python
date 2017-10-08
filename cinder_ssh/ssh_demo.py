from cinder import ssh_utils
from oslo.config import cfg
import eventlet
from eventlet import greenthread
import greenlet


CONF = cfg.CONF
CONF(default_config_files=['/etc/cinder/cinder.conf'])


def with_timeout(f):
    @functools.wraps(f)
    def __inner(self, *args, **kwargs):
        timeout = kwargs.pop('timeout', None)
        gt = eventlet.spawn(f, self, *args, **kwargs)
        if timeout is None:
            return gt.wait()
        else:
            kill_thread = eventlet.spawn_after(timeout, gt.kill)
            try:
                res = gt.wait()
            except greenlet.GreenletExit:
                raise exception.VolumeBackendAPIException(
                    data="Command timed out")
            else:
                kill_thread.cancel()
                return res

    return __inner


    @with_timeout
    def _ssh_execute(self, ssh, command, *arg, **kwargs):
        transport = ssh.get_transport()
        chan = transport.open_session()
        completed = False

        try:
            chan.invoke_shell()

            LOG.debug("Reading CLI MOTD")
            self._get_output(chan)

            cmd = 'stty columns 255'
            LOG.debug("Setting CLI terminal width: '%s'", cmd)
            chan.send(cmd + '\r')
            out = self._get_output(chan)

            LOG.debug("Sending CLI command: '%s'", command)
            chan.send(command + '\r')
            out = self._get_output(chan)

            completed = True

            if any(ln.startswith(('% Error', 'Error:')) for ln in out):
                desc = _("Error executing EQL command")
                cmdout = '\n'.join(out)
                LOG.error(_LE("%s"), cmdout)
                raise processutils.ProcessExecutionError(
                    stdout=cmdout, cmd=command, description=desc)
            return out
        finally:
            if not completed:
                LOG.debug("Timed out executing command: '%s'", command)
            chan.close()




sshpool = ssh_utils.SSHPool(
                "192.168.1.48",
                2222,
                10,
                "root",
                password="password",
                privatekey="/root/.ssh/id_dsa");

#                min_size=min_size,
#                max_size=max_size)


#paramiko.client.SSHClient
with sshpool.item() as ssh:
    b=ssh.get();
    #print b;
