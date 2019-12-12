<h1>StreaMoor API documentation</h1>
<h2>Getting started</h2>
This API is designed to be implemented with the StreaMoor streaming service for any frontend basically.
<br>
All operations are done through routes, every route has their specific method that they can reply.
Each basic operation has their own route that are descibed below.
<h2>Routes</h2>
<h3>login</h3>
Method = 'post'<br>
    Gets the data from the login form and authorizes the input<br>
    Returns: JSON with auth result info that can be one of two:
    <li> result='fail' if the authorization was unsucceful due to incorrect email or password
    <li> result = user_nick returns the nickname to display if the auth was successful
<h3>Register</h3>
Method = 'post'<br>
Inserts the information about new user unto the database<br>
Returns JSON with the result that can be one of two:
    <li> result = 'bad' if the user already exists
    <li> result ='good' if the user gets successfuly registered and he's been put in the database
<h3>subscibe</h3>
Subscibes the user to the channel
<h3>unsubscibe</h3>
Unsubscibes the user from the channel
<h3>channels</h3>
method = 'get'<br>
 Gets the channels that are in the hub selected <br>
Returns JSON with the channels
<h3>channel</h3>
method = 'get'<br>
Gets the channel info from the database and returns info about it <br>
Returns JSON with the channel info: nickname, subs, description, curr_hub
<h3>video_feed</h3>
Generates the video image from the webcam and sends it to the channel<br>
Returns the next frame to be put in the 'img' tag
<h3>search</h3>
method = 'get' <br>
Searches the database for anything that is similar to the search input <br>
Returns: channels that might fit the search input
<h2>Database methods</h2>
Class SQLModel contains methods to work with the Database, in this case it's POSTGRES
<h3>connect</h3>
Private class method<br>
Connects to the database <br>
Returns connection to the database
<h3>query</h3>
Performs a query than us not specified in the other methods<br>
Arguments:
<li> query: the SQL query to be executed
<li> attrs: any attributes to be added to the query during the execute() method
Returns: the result of the query
<h3>normalize_cols</h3>
Class method
Changes columns presentation to be correct for the query <br>
Arguments:
<li>cols: columns to be normalized
<h3>insert</h3>
Class method <br>
Insert the values in the database <br>
Arguments:
<li>values: values to be inserted to the database
<h3>get_by_attrs</h3>
Class method<br>
Gets the values from the database that correspond to the values given<br>
Arguments:
<li>cols: columns to be selected from the database
<li>attr_cols: columns that are used in the WHERE statement
<li>attr_values: values that are used in the WHERE statement in corresponding columns
<li>group_by: None by default, GROUP BY statement
<li>order_by: None by default, ORDER BY statement
<br> Has 4 overloads depending on the group_by and order_by, these overloads contain defferent queries<br>
Returns: tuple with the query result
<h3>update_by_attrs</h3>
Class method<br>
Updates the values in the database that correspond to the values given<br>
Arguments:
<li>columns: columns to be updated
<li>values: values to be put in the database
<li>attr_cols: columns that are used in the WHERE statement
<li>attr_values: values that are used in the WHERE statement
<h3>delete_by_attrs</h3>
Class method<br>
Deletes the rows from the database that correspond to the values given<br>
Arguments:
<li>attr_cols: columns that are used in the where statement
<li>attr_values: columns that are used in the statement
 



