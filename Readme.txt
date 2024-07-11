Note: 	I provided an Insomnia file: Insominia_CAPSTONE.json at capstone-venv/littlelemon/
      	so you can use it in your Insomnia Client.
	All require token authentication, hence 'AUTH' in request's names, tokens are included.
Note: 	To activate the venv you may need to update the pyvenv file, because I used python 3.10.14

The file contains these endpoints:
/restaurant/api-token-auth/	POST (to query a token)
/auth/users/			GET (to query user(s))
/restaurant/menu/		GET (to query items) 	POST (to add 1 item)
/restaurant/menu/3		PUT (to query 1 item) 	DEL (to delete 1 item)
/restaurant/booking/tables/	GET (to query bookings)