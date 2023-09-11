# see what distibution we are using


def distribution():
	"""Provides distribution info and handles missing support for linux_distribution() in platform package for python 3.8+"""
	import platform
	try:
		return platform.linux_distribution()
	except AttributeError:
		import distro
		return distro.linux_distribution()

print(distribution())
