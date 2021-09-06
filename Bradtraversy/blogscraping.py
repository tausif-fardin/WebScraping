from bs4 import BeautifulSoup

html_doc = """
<html>

<head>
    <title>Registration Page </title>
</head>

<body>
<h1>My Registration Page</h1>
    <div>
        <table>
            <tr>
                <td>Name:</td>
                <td><input type="text" name="firstName"></td>
            </tr>
            <tr>
                <td>Email:</td>
                <td><input type="text" name="email"></td>
            </tr>
            <tr>
                <td>User Name:</td>
                <td><input type="text" name="userName"></td>
            </tr>
            <tr>
                <td>Password:</td>
                <td><input type="password" name="passsword"></td>
            </tr>
            <tr>
                <td>Confirm Password:</td>
                <td><input type="password" name="cpassword"></td>
            </tr>
            <tr>
                <td>Gender</td>
                <td><input type="radio" id="male" name="gender" value="male">
                    <label for="male">Male</label>
                    <input type="radio" id="female" name="gender" value="female">
                    <label for="female">Female</label>
                    <input type="radio" id="other" name="gender" value="other">
                    <label for="other">Other</label>

                </td>
            </tr>
            <tr>
                <td>Date of Birth <br></td>
                <td><input type="date" name="birthday"></td>
            </tr>
            <tr>

                <td><input type="submit" value="submit">
                    <input type="reset">
                </td>


            </tr>

        </table>
    </div>
</body>

</html>


"""

soup = BeautifulSoup(html_doc, 'html.parser')
# Direct
# print(soup.body)
# print(soup.head)
# print(soup.head.title)


# find()
# el = soup.find('div')  # only return the first element (first div)

# find more than or all
#find_all() or findAll()

el1 = soup.find_all('div')
print(el1)
# specific div such as this returns the second div
#el1 = soup.find_all('div')[1]
# print(el1)

# select by id or class
#el2 = soup.find(id='id_name')
# class is a reserve word in python so we have to use an underscore
#el3 = soup.find(class_='class_name')

# select by attribute name
#el4 = soup.find(attrs={"attribute-name": "valueofattribute"})

# select for css
# el5 = soup.select('#idname')

# select without list
# el6 = soup.select('#idname')[0]

# select for class
#el7 = soup.select('.classname')[0]

# get_text()
el8 = soup.find('table').get_text()
print(el8)

# loop
for i in soup.select('.item'):
    print(i.get_text())

# navigation
el = soup.body.contents[0]  # it reads linebreaks as well
el = soup.body.contents[0].next_sibling  # find the next element
el = soup.body.contents[0].find_next_sibling()  # find the next element
# find the previous element (contents[0])
el = soup.body.contents[1].find_previous_sibling()

# get the parent element
el = soup.find(class_='itemname').find_parent()

# specify what to look from
el = soup.find(class_='itemname').find_next_sibling(
    'p')  # return next paragraph
