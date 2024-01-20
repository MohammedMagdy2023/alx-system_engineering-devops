# kill a processor

exec {'kill processor':
command => 'pkill killmenow',
}
