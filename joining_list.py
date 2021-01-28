# joining list of library dependencies to use with `pkg-config`

dependencies = [
	('libzmq', '>= 4.0.5'),
	('libavformat', '>= 56.1.0'),
	('libavutil', '>= 54.3.0'),
	('libavcodec', '>= 56.1.0'),
	('jsoncpp', '>= 0.6.0'),
	('libsoup-2.4', '>= 2.48.0'),
	'libjpeg',
	'libgcrypt',
	'libmosquitto',
]

pkg_conf = 'pkg-config --cflags --libs ' + ' '.join(
	map(lambda dep: dep[0] if type(dep) == tuple else dep, dependencies))

print(pkg_conf)
