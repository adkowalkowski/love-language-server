# Project Overview

## Frontend Repository
This repository is for the backend, visit the [frontend repository](https://github.com/adkowalkowski/love-language-client)

## Deployed Link
Visit the [Love Language Directory](https://adkowalkowski.github.io/love-language-client/)

## Project Schedule

| Day   | Deliverable                          | Status     |
| ----- | ------------------------------------ | ---------- |
| Day 1 | Planning and Approval                | Complete |
| Day 2 | Set up backend files and structure, test and deploy backend | Complete |
| Day 3 | Set up frontend files, connect frontend with backend, begin MVP attainment | Complete |
| Day 4 | Attain MVP, debug MVP, begin styling | Complete |
| Day 5 | Finalize CSS Styling and Responsive Design, begin postMVP if MVP attained | Complete |
| Day 6 | Confirm finalized MVP & Bug Fixes | Complete |
| Day 7 | Final Touches and deploying frontend | Incomplete |
| Day 8 | Presentation | Complete |

## Project Description

Love language Directory is an app that allows users to create an account, and then add their top 5 love languages. Users can also search for other users and view their top 5 love languages. 

This app will include a backend database using SQL and Django and a frontend web application using React.js.

## User Stories

Taken from the official [5 love languages website](https://www.5lovelanguages.com/learn): "different people with different personalities give and receive love in different ways. By learning to recognize these preferences in yourself and in your loved ones, you can learn to identify the root of your conflicts, connect more profoundly, and truly begin to grow closer."

The user of this app values how love languages can impact relationships (both friendship and romantic). However, it is very hard to keep track of your social network's love languages; it's even hard to remember your own love languages! Users of this application look for a centralized place where they can easily access their top 5 love languages as well as their social network's love languages.  

## Wireframes

- [Mobile & Desktop](https://imgur.com/a/BzuPnNO)

## React Architecture
- [React Architecture](https://imgur.com/a/yGqyY6x) 

### MVP/PostMVP

#### MVP

- 2 models for data (User, Love)
- Fully functional user authentication (token) (signup, signin, signout, changepassword, deleteaccount)
- Ability to search by email 
- CRUD functionality (Add User/Love, View Love, Edit User/Love, Delete Love)
- Routes and components on frontend 
- Fetch data from backend API
- Responsive design from mobile to desktop
- Use React bootstrap for design
- Fully Deployed frontend and backend

#### PostMVP

- Social network system (add friends so you can see their love languages without searching)

## Models

```py

# Example from lecture
class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        """Return string representation of the user"""
        return self.email

class Love(models.Model):
    one: models.CharField(max_length=100)
    two: models.CharField(max_length=100)
    three: models.CharField(max_length=100)
    four: models.CharField(max_length=100)
    five: models.CharField(max_length=100)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )

    dunder method 
```

## Routing Table

| **URL**     | **HTTP Verb** | **Description** |
| ----------- | ------------- | ---------------- |
| /sign-up | POST | Sign up a new user |
| /sign-in | POST | User sign in |
| /sign-out | DELETE | User sign out |
| /change-password | PATCH | User change password |
| /love-languages | POST | Add 5 love languages to user's account |
| /love-languages | GET | View 5 love languages of user's account |
| /love-languages/<str:email> | GET | View 5 love languages of any user |
| /love-languages/modify/<int:pk> | DELETE | Delete 5 love languages of signed-in user |
| /love-languages/modify/<int:pk> | PUT | Update 5 love languages of signed-in user |

## Functional Components 

| Component                      |                   Description                    |
| ------------------------------ | :----------------------------------------------: |
| Home | Landing Page for a signed-in user, can submit/edit their top5 |
| SignUp | Page to signup a new user |
| SignIn |  Page to signin a user  |
| AddForm |  Component that holds the form to add a user's top5 |
| UpdateForm |  Component that holds the form to update a user's top5 |
| Search | Page with a searchbox and then will return that user's top5 if the user is found |
| About | About the site and creator |
| FAQ | Frequently asked questions |
| Header | Logo and Menu |

#### MVP (all in hrs unless otherwise stated)

| Task                          | Priority | Estimated Time | Actual Time |
| ---------------------------------- | :------: | :------------: | :---------: |
| Installing and Setup for backend   |    H     |      1       |      1     |
| Models                             |    H     |      4       |      4     |
| CRUD Routes and testing on Postman |    H     |      5       |      5    |
| Deploying backend                  |    H     |     2      |           |
| Creating React App                 |    H     |      1       |      1     |
| Add Routes                         |    H     |      2       |     2      |
| Create Components                  |    H     |      5       |     2      |
| Connect user authentication on front-end                  |    H     |      10       |     10      |
| Fetch and test data on frontend    |    H     |      5       |      10     |
| Search by user on front-end    |    H     |      5       |     10      |
| Responsive Design                  |    H     |      4       |     5      |
| CSS and Bootstrap                  |    H     |      4       |     4      |
| Deploy frontend                    |    H     |      1       |           |
| Total                              |    N/A     | 49 |           |

#### PostMVP (all in hrs unless otherwise stated)

| Task            | Priority | Estimated Time | Actual Time |
| -------------------- | :------: | :------------: | :---------: |
| Social network features              |    M    |      40       |           |
| Total                |    N/A     |      40      |           |

## Additional Libraries
React Bootstrap
Formik (not currently in use, need to debug)
Axios


## Code Snippet
I have a fair amount of conditional rendering and I'm happy with how it turned out -- one example is on sign in. There is conditional rendering on the profile page: if a user is not signed in, it renders the sign in page. Once a user signs in, the sign in function reloads the page and the profile page will render.

Sign in handler
```js
 const SignIn = () => {
  
  // STATE FOR USER SIGN IN

  const [user, setUser] = useState({
    email: "",
    password: "",
  })

  // HANDLERS FOR POST

  const handleFormChange = (e) => {
    e.preventDefault();
    e.persist();
    setUser((prevUser) => {
      const editedUser = {
        ...prevUser,
        [e.target.name]: e.target.value,
      };
      return editedUser;
    });
  };


  const handleFormSubmit = (e) => {
    e.preventDefault();
    const userData = {
      email: user.email,
      password: user.password
    };
     axios
      .post("http://127.0.0.1:8000/sign-in/", userData)
      .then((response) => {
        setUser(response.data);
        localStorage.setItem('token', response.data.user.token)
        console.log(localStorage)
        console.log(user)
        window.location.reload(true)
      })
      .catch((err) => {
        alert('Incorrect login information')
        console.log(err);
      });
  };
```
And the conditional rendering on the profile page: 
```js
// CONDITIONAL RENDERING IF A USER IS/IS NOT SIGNED IN

  if (!token) {
    return (
      <div className="not-signed-in">
        <Alert variant="danger" onClose={() => setShow(false)} >
        <Alert.Heading>Sign in to view your profile</Alert.Heading>
      </Alert>
        <SignIn />
      </div>
    );
  }

  if (token) {
    return (

      // FORM FOR SIGNED IN USER TO ADD THEIR TOP 5
      
      <div className="top-five-form">
        <Form onSubmit={handleTopFiveSubmit}>
          <Form.Label>To add your top 5 love languages into our directory, fill out the form below</Form.Label>
          <Form.Select
            onChange={handleOneSelect}
            aria-label="Default select example"
          >
            <option>Number One</option>
            <option>Acts of Service</option>
            <option>Quality Time</option>
            <option>Words of Affirmation</option>
            <option>Receiving Gifts</option>
            <option>Physical Touch</option>
          </Form.Select>
          <Form.Select
            onChange={handleTwoSelect}
            aria-label="Default select example"
          >
            <option>Number Two</option>
            <option>Acts of Service</option>
            <option>Quality Time</option>
            <option>Words of Affirmation</option>
            <option>Receiving Gifts</option>
            <option>Physical Touch</option>
          </Form.Select>
          <Form.Select
            onChange={handleThreeSelect}
            aria-label="Default select example"
          >
            <option>Number Three</option>
            <option>Acts of Service</option>
            <option>Quality Time</option>
            <option>Words of Affirmation</option>
            <option>Receiving Gifts</option>
            <option>Physical Touch</option>
          </Form.Select>
          <Form.Select
            onChange={handleFourSelect}
            aria-label="Default select example"
          >
            <option>Number Four</option>
            <option>Acts of Service</option>
            <option>Quality Time</option>
            <option>Words of Affirmation</option>
            <option>Receiving Gifts</option>
            <option>Physical Touch</option>
          </Form.Select>
          <Form.Select
            onChange={handleFiveSelect}
            aria-label="Default select example"
          >
            <option>Number Five</option>
            <option>Acts of Service</option>
            <option>Quality Time</option>
            <option>Words of Affirmation</option>
            <option>Receiving Gifts</option>
            <option>Physical Touch</option>
          </Form.Select>
          <Button className="submit-button" variant="secondary" type="submit">
            Submit
          </Button>
        </Form>

        {/* // BUTTON TO VIEW A SIGNED IN USER'S TOP FIVE */}

        <div>
          <Button className="top-five-button" variant="secondary" onClick={handleGet}>
            View Your Top 5
          </Button>
          {topFiveList}
        </div>
      </div>
    );
  }
```

## Issues and Resolutions
My project has users add their top 5 love languages via a form. Since there are limited options and my model requires them to be entered verbatim, I'm going to use a select/dropdown form. Originally I had one state to store each of these values, but I couldn't get the selected dropdown data to update the state
```js
const AddTopFive = () => {

  // CONDITIONAL RENDERING COULD BE if (!token) render SignIn page if(token) render AddTopFive 
  const token = localStorage.token
  console.log(token)

  const [topFive, setTopFive] = useState({
      one: "",
      two: "",
      three: "",
      four: "",
      five: ""
  })
  
//   const handleSelect = (e) => {
//     setTopFive((prevTopFive) => {
       setTopFive(e)
//     }
//   };

  const handleTopFiveSubmit = () => {
    const topFiveData = {
      one: topFive.one,
      two: topFive.two,
      three: topFive.three,
      four: topFive.four,
      five: topFive.five
    };
     axios
      .post("http://127.0.0.1:8000/love-languages/", topFiveData, {
          headers: {
            'Authorization': `Token ${token}` 
          }
      })
      .then((response) => {
        setTopFive(response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="top-five-form">
      <Form onSubmit={handleTopFiveSubmit} onSelect={handleSelect}>
      <Form.Select aria-label="Default select example">
        <option>Number One</option>
        <option value="1">Acts of Service</option>
        <option value="2">Quality Time</option>
        <option value="3">Words of Affirmation</option>
        <option value="4">Receiving Gifts</option>
        <option value="5">Physical Touch</option>
      </Form.Select>
      <Form.Select aria-label="Default select example">
        <option>Number Two</option>
        <option value="1">Acts of Service</option>
        <option value="2">Quality Time</option>
        <option value="3">Words of Affirmation</option>
        <option value="4">Receiving Gifts</option>
        <option value="5">Physical Touch</option>
      </Form.Select>
      <Form.Select aria-label="Default select example">
        <option>Number Three</option>
        <option value="1">Acts of Service</option>
        <option value="2">Quality Time</option>
        <option value="3">Words of Affirmation</option>
        <option value="4">Receiving Gifts</option>
        <option value="5">Physical Touch</option>
      </Form.Select>
      <Form.Select aria-label="Default select example">
        <option>Number Four</option>
        <option value="1">Acts of Service</option>
        <option value="2">Quality Time</option>
        <option value="3">Words of Affirmation</option>
        <option value="4">Receiving Gifts</option>
        <option value="5">Physical Touch</option>
      </Form.Select>
      <Form.Select aria-label="Default select example">
        <option>Number Five</option>
        <option value="1">Acts of Service</option>
        <option value="2">Quality Time</option>
        <option value="3">Words of Affirmation</option>
        <option value="4">Receiving Gifts</option>
        <option value="5">Physical Touch</option>
      </Form.Select>
      <Button variant="primary" type="submit">
            Submit
          </Button>
      </Form>
      
    </div>
  );
};

export default AddTopFive;
```
I messed around trying to push into an array, but couldn't get that to work. I came up with a verbose workaround where I have five separate states and five separate handleSelect methods. It's still working as intended and that's a win.
```js
const [one, setOne] = useState("");
  const [two, setTwo] = useState("");
  const [three, setThree] = useState("");
  const [four, setFour] = useState("");
  const [five, setFive] = useState("");

  const handleOneSelect = (e) => {
    e.preventDefault();
    e.persist();
    const selectedValue = e.target.value;
    console.log(selectedValue);
    setOne(selectedValue);
  };

  const handleTwoSelect = (e) => {
    e.preventDefault();
    e.persist();
    const selectedValue = e.target.value;
    console.log(selectedValue);
    setTwo(selectedValue);
  };

  const handleThreeSelect = (e) => {
    e.preventDefault();
    e.persist();
    const selectedValue = e.target.value;
    console.log(selectedValue);
    setThree(selectedValue);
  };

  const handleFourSelect = (e) => {
    e.preventDefault();
    e.persist();
    const selectedValue = e.target.value;
    console.log(selectedValue);
    setFour(selectedValue);
  };

  const handleFiveSelect = (e) => {
    e.preventDefault();
    e.persist();
    const selectedValue = e.target.value;
    console.log(selectedValue);
    setFive(selectedValue);
  };

  const handleTopFiveSubmit = () => {
    const topFiveData = {
      one: one,
      two: two,
      three: three,
      four: four,
      five: five,
    };
    axios
      .post("http://127.0.0.1:8000/love-languages/", topFiveData, {
        headers: {
          Authorization: `Token ${token}`,
        },
      })
      .then((response) => {
        setOne(response.data.one);
        setTwo(response.data.two);
        setThree(response.data.three);
        setFour(response.data.four);
        setFive(response.data.five);
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="top-five-form">
      <Form onSubmit={handleTopFiveSubmit}>
        <Form.Select
          onChange={handleOneSelect}
          aria-label="Default select example"
        >
          <option>Number One</option>
          <option>Acts of Service</option>
          <option>Quality Time</option>
          <option>Words of Affirmation</option>
          <option>Receiving Gifts</option>
          <option>Physical Touch</option>
        </Form.Select>
        <Form.Select
          onChange={handleTwoSelect}
          aria-label="Default select example"
        >
          <option>Number Two</option>
          <option>Acts of Service</option>
          <option>Quality Time</option>
          <option>Words of Affirmation</option>
          <option>Receiving Gifts</option>
          <option>Physical Touch</option>
        </Form.Select>
        <Form.Select
          onChange={handleThreeSelect}
          aria-label="Default select example"
        >
          <option>Number Three</option>
          <option>Acts of Service</option>
          <option>Quality Time</option>
          <option>Words of Affirmation</option>
          <option>Receiving Gifts</option>
          <option>Physical Touch</option>
        </Form.Select>
        <Form.Select
          onChange={handleFourSelect}
          aria-label="Default select example"
        >
          <option>Number Four</option>
          <option>Acts of Service</option>
          <option>Quality Time</option>
          <option>Words of Affirmation</option>
          <option>Receiving Gifts</option>
          <option>Physical Touch</option>
        </Form.Select>
        <Form.Select
          onChange={handleFiveSelect}
          aria-label="Default select example"
        >
          <option>Number Five</option>
          <option>Acts of Service</option>
          <option>Quality Time</option>
          <option>Words of Affirmation</option>
          <option>Receiving Gifts</option>
          <option>Physical Touch</option>
        </Form.Select>
        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
```



