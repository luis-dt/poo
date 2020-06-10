
class Lamp:

	_LAMPS = ['''
          .
     .    |    ,
      \\  '   /
       ` ,-. '
    --- (   ) ---
        \\ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \\/
        _|=|_
       |_____|
    ''']

	def __init__(self):
		
		self._is_turn_on = False

		def turn_on(self):
			self._is_turn_on = True
			self._display_image()

		def turn_off(self):
			self._is_turn_on = False
			self._display_image()

		def _display_image():
			if self._is_turn_on == True:
				print(self._LAMPS[0])
			else:
				print(self._LAMPS[1])	
		