# -*- coding: utf-8 -*-

class Emitter:
    def __init__(self):
        self._handlers = {}
    
    def on(self, signal, handler):
        self._handlers[signal] = handler
    
    def emit(self, signal, data):
        func = self._handlers.get(signal)
        if func is None:
            raise ValueError('Wrong emit key')
        return func(data)


def print_connected(data):
    print('first: {0}'.format(data))


def print_disconnected(data):
    print('second: {0}'.format(data))

if __name__ == '__main__':
    emitter = Emitter()
    emitter.on('connect', print_connected)
    emitter.on('disconnect', print_disconnected)
    emitter.emit('connect', 'http-server')
    # prints to console:
    # > We have been connected to http-server
    emitter.emit('connect', 'websocket')
    # prints to console:
    # > We have been connected to websocket

    emitter.emit('disconnect', 'websocket')
    # prints to console:
    # > We disconnected from websocket
    emitter.emit('disconnect', 'http-server')
    # prints to console:
    # > We disconnected from http-server
