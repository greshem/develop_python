import urllib;
def slackmsg(msg):
	URL="https://slack.com/api/chat.postMessage"
	SUFFIX="username=watchbird&icon_emoji=%3Abirdno%3A&pretty=1"
	CHANNEL="C10GZ75BP"
	TOKEN="xoxp-34036332497-34021439412-37746432451-c2cd827677"

	msgstr = "token={t}&channel={c}&text={m}&{s}".format(
	t=TOKEN,
	c=CHANNEL,
	m=urllib.quote(msg),
	s=SUFFIX
	)
	print msgstr
	print "curl -d'{m}' {u}".format(m=msgstr, u=URL);

slackmsg("bbb");
