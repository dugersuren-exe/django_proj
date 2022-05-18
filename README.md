<details open>
<summary>1. Орчноо бэлдэх</summary>

Орчноо бэлдэхийн тулд эхлээд дараах командуудыг суулгах хэрэгтэй.

* python -ийг суулгах
* pip -ийг ашиглан django-г суулгах
 
**Анхаарах зүйл:**

Windows үйлдлийн систем дээр python-ийг суулгахдаа дараах зүйлийг анхаарах хэрэгтэй.
Татаж авсан install-ийг уншуулахдаа **Add Python 3.10 to PATH** гэсэн сонголтыг сонгож Install Now товчийг дарж суулгана. Жишээг доор зургаар харуулав.
![](img/install.png)
**Нэмэлт сангуудаа суулгах:**

* django- г суулгах команд

```
pip install django
```

</details>

---

<details>
<summary>2. Прожектоо үүсгэх</summary>

Идэвхитэй байгаа фолдер дотор прожектийг үүсгэхдээ дараах командын тусламжтайгаар үүсгэдэг. Иймээс эхлээд тухайн фолдер дотор очиж дараах командыг өгөх ёстой.

Comandline дээр тухайн фолдерт очихдоо

"Start+R" товчлуурын тусламжтайгаар гарч ирэх **Run** цонхон дээр **cmd** гэж бичээд ажиллуулах

Идэвхитэй байгаа фолдероос гарах
```
cd..
```

Тухайн фолдер дотор байгаа <folder_name> нэртэй фолдер руу орох.

```
cd <folder_name>
```


**Прожект үүсгэх:**

Дараах командын тусламжтайгаар <project_name> нэртэй шинэ прожект үүсдэг.


```
django-admin startproject <project_name>
```

**Жишээ нь:**

```
django-admin startproject main_project
```


</details>

---

<details>
<summary> 3. Прожектоо ажиллаж байгаа эсэхийг шалгах, тестлэх </summary>

Прожектоо ажиллаж байгаа эсэхийн шалгахын тулд **Commandline** дээрээ тухайн прожектийн гадна талын хавтас руу нэвтэрсний дараа дараах командыг өгнө.

```
python manage.py runserver
```

</details>



---

<details>
<summary> 4. Прожект дортор шинэ app-ийг үүсгэх</summary>
Прожект дотор олон app-ийг нэмж оруулах боломжтой бөгөөд дараах командын өгч үүсгэх боломжтой.


**Прожект дотор app-ийг үүсгэх команд:**

```
python manage.py startapp <app_name>
```
**Жишээ нь : **

```
python manage.py startapp main
```

**Прожектийг нэгтгэх**

Дараах командын тусламжтайгаар прожектод хийгдсэн өөрчлөлтийг, гол төлөв өгөгдлийн бааз дээр хийгдсэн өөрчлөлт болон моделийг өөрчлөн хадгалах боломжтой.

```
python manage.py makemigrations main
```

Бааз руу хадгалах нэгтгэх 





</details>

---

<details>
<summary> 5. Прожектоо app-тай холбох </summary>

<proj_name> фолдер дотор байгаа **urls** дотор дараах байдлаар үндсэн app-ийн urls-ийг холбож өгнө.

```
path('', include('main.urls')),
```


**Жишээ нь:**

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('main.urls')), # main will be the name of your app
    path('admin/', admin.site.urls),
]
```

Мөн үндсэн app-ийн **urls** дотор view-ийг дуудах холбоосыг холбоосыг оруулж болно.

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]

```
app-ийн views файл дотор view буюу харагдацуудыг дуудах холбоосыг оруулж өгнө.

**Жшиээ нь:**

```
# views.py file
from django.http import HttpResponse


def index(request):
    return HttpResponse("<div>Энэ бол миний анхны сайт юм!</div>")

def about(request):
    return HttpResponse("<div> Энэ бол about хуудас</div>")

```


</details>

---

<details>
<summary> 6. ____________</summary>
Жишээ нь:



pages/api фолдер дотор 
   * words.js

**words.js**

```
const { connectToDatabase } = require('../../utils/connectDb');
const ObjectId = require('mongodb').ObjectId;

export default async function handler(req, res) {
    // switch the methods
    switch (req.method) {
        case 'GET': {
            return getPosts(req, res);
        }

        case 'POST': {
            return addPost(req, res);
        }

        case 'PUT': {
            return updatePost(req, res);
        }

        case 'DELETE': {
            return deletePost(req, res);
        }
    }
}

// Getting all posts.
async function getPosts(req, res) {
    try {
        let { db } = await connectToDatabase();
        let words = await db
            .collection('words')
            .find({})
            .sort({ published: -1 })
            .toArray();
        return res.json({
            message: JSON.parse(JSON.stringify(words)),
            success: true,
        });
    } catch (error) {
        return res.json({
            message: new Error(error).message,
            success: false,
        });
    }
}

// Adding a new post
async function addPost(req, res) {
    try {
        let { db } = await connectToDatabase();
        console.log("hi----->",req.body);
        await db.collection('words').insertOne(req.body);
        
        return res.json({
            message: 'Post added successfully',
            success: true,
        });
    } catch (error) {
        return res.json({
            message: new Error(error).message,
            success: false,
        });
    }
}

// Updating a post
async function updatePost(req, res) {
    try {
        let { db } = await connectToDatabase();

        await db.collection('words').updateOne(
            {
                _id: new ObjectId(req.body),
            },
            { $set: { published: true } }
        );

        return res.json({
            message: 'Post updated successfully',
            success: true,
        });
    } catch (error) {
        return res.json({
            message: new Error(error).meзүssage,
            success: false,
        });
    }
}

// deleting a post
async function deletePost(req, res) {
    try {
        let { db } = await connectToDatabase();

        await db.collection('words').deleteOne({
            _id: new ObjectId(req.body),
        });

        return res.json({
            message: 'Post deleted successfully',
            success: true,
        });
    } catch (error) {
        return res.json({
            message: new Error(error).message,
            success: false,
        });
    }
}



```



</details>

---

<details>
<summary> ________________ </summary>

Тухайн сайт нь өгөглийн баазтай зөв холбосон бол дараах холбоосоор орж шалгах ажиллаж байгаа эсэхийг нь шалгаж үзээрэй.
Үүгийг веб броузерээс бол зөвхөн get-ээр дуудан ажиллуулах боломжтой байдаг. 

Иймд GET, PUT, POST, DELETE method-оор дуудан тест хийж үзэхийн тулд **POSTMAN** програмыг ашиглаж болно.

**Жишээ нь:**

GET method -оор  броузер дээр ажиллуулан шалгаж болдог учир дараах холбоосыг броузерийн addressbar дээр бичиж ажиллуулж үзээрэй:    
```
http://localhost:3000/api/words
```
Үүнийг ажиллуулахад өгөгдлийн бааз дахь өгөгдлүүдийн жагсаалт нь JSON форматаар дуудагдан харагдах боломжтой байдаг.

</details>

---


<details>
<summary> ____________________ </summary>

Үндсэн фолдер дотор redux фолдер бүхий агуулгуудыг үүсгэж холбох

**Жишээ нь:**
өмнөх хичээл дээр ашиглаж байсан redux - фолдерийг үндсэн фолдер дотор хуулаад тэндээ тохиргоо хийж болно. Өмнө нь үүсгэсэн redux фолдер нь дараах бүтэцтэй байгаа.

* redux/pupil/actionCreator.js
* redux/pupil/actions.js
* redux/pupil/reducers.js
* redux/rootReducer.js
* redux/store.js

Энд өмнө нь pupil redux нь JSON файлаас өгөгдөл уншиж чаддаг байдлаар зохион байгуулалт хийж байсан.

Үүний холболтыг _app.js файл дотор холбон тохируулж өгөх шаардлагатай байдаг.

Жишээ нь: 
**_app.js файл дотор дараах агуулга орсон байх**
```
import { Provider } from "react-redux";
import { createWrapper } from "next-redux-wrapper";
import store from "../redux/store";

import 'antd/dist/antd.css';

function MyApp({ Component, pageProps }) {
  return (
    <Provider store={store}>
      <Component {...pageProps} />
    </Provider>
  );
} 

const makeStore = () => store;
const wrapper = createWrapper(makeStore);

 

export default wrapper.withRedux(MyApp);
```

</details>

---
<details>
<summary> ______________ </summary>

redux фолдер дотор words фолдерийг үүсгэж дотор нь дараах 3 файлыг үүсгэнэ.
* actions.js
* actionCreator.js
* reducers.js


 
**Жишээ нь:**

actions.js файлын агуулга
```
const actions = {
  WORDS_LOADING: 'WORDS_LOADING',
  WORDS_SUCCESS: 'WORDS_SUCCESS',
  WORDS_ERROR: 'WORDS_ERROR',

  wordsLoading: () => {
    return {
      type: actions.WORDS_LOADING,
    };
  },

  wordsSuccess: data => {
    return {
      type: actions.WORDS_SUCCESS,
      data,
    };
  },

  wordsError: err => {
    return {
      type: actions.WORDS_ERROR,
      err,
    };
  },
  

};

export default actions;

```

actionCreator.js
```
import actions from './actions';
import axios from 'axios'

const { wordsLoading, wordsSuccess, wordsError } = actions;


const getAllWords = () => {
  
  return async dispatch => {
    try {
      dispatch(wordsLoading());
      await axios.get("http://localhost:3000/api/words").then(({data}) => {          
        dispatch(wordsSuccess(data.list))
      });
    } catch (err) {
      dispatch(wordsError(err));
    }

  };
};



export {getAllWords };


```


reducers.js
```
import actions from './actions';

const { WORDS_LOADING, WORDS_SUCCESS, WORDS_ERROR} = actions;

const initialState = {
  list: [],
  loading: false,
  error: null
};

const WordsReducer = (state = initialState, action) => {
    
  const { type, data, err } = action;
  //console.log('==========>',data)   
  switch (type) {
    case WORDS_LOADING:
      return {
        ...state,
        loading: true,
        error: null,
        
      };
    case WORDS_SUCCESS:   
      return {
        ...state,
        list: data,
        loading: false,
      };     
    case WORDS_ERROR:
      return {
        ...state,
        error: err,
        loading: false

      };
    
    default:
      return state;
  }
};
export default WordsReducer;




```

</details>

---


<details>
<summary>  _____________ </summary>

Үндсэн фолдер дотор **/components/layouts/MainLayout.js**  -ийг үүсгэх
Энэ нь тухайн хуудасны гадна талаар тойрон байрлах учир энэ хуудсан дэээр голдуу үндсэн цэс болон хуудас бүр дээр байдаг агуулгуудыг оруулах нь тохиромжтой байдаг.

Жишээ нь ant.design-ийн Layout-ийг ашиглан загварчласан жишээг доор үзүүллээ.

**Жишээ нь:**
```
import { Layout, Menu, Breadcrumb } from 'antd';
import { UserOutlined, LaptopOutlined, NotificationOutlined } from '@ant-design/icons';
import { Children } from 'react';

const { SubMenu } = Menu;
const { Header, Content, Footer, Sider } = Layout;

function MainLayout({children}) {
  return (
    <Layout>
    <Header className="header">
      <div className="logo" />
      <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
        <Menu.Item key="1">nav 1</Menu.Item>
        <Menu.Item key="2">nav 2</Menu.Item>
        <Menu.Item key="3">nav 3</Menu.Item>
      </Menu>
    </Header>
    <Content style={{ padding: '0 50px' }}>
      <Breadcrumb style={{ margin: '16px 0' }}>
        <Breadcrumb.Item>Home</Breadcrumb.Item>
        <Breadcrumb.Item>List</Breadcrumb.Item>
        <Breadcrumb.Item>App</Breadcrumb.Item>
      </Breadcrumb>
      <Layout className="site-layout-background" style={{ padding: '24px 0' }}>
        <Sider className="site-layout-background" width={200}>
          <Menu
            mode="inline"
            defaultSelectedKeys={['1']}
            defaultOpenKeys={['sub1']}
            style={{ height: '100%' }}
          >
            <SubMenu key="sub1" icon={<UserOutlined />} title="subnav 1">
              <Menu.Item key="1">option1</Menu.Item>
              <Menu.Item key="2">option2</Menu.Item>
              <Menu.Item key="3">option3</Menu.Item>
              <Menu.Item key="4">option4</Menu.Item>
            </SubMenu>
            <SubMenu key="sub2" icon={<LaptopOutlined />} title="subnav 2">
              <Menu.Item key="5">option5</Menu.Item>
              <Menu.Item key="6">option6</Menu.Item>
              <Menu.Item key="7">option7</Menu.Item>
              <Menu.Item key="8">option8</Menu.Item>
            </SubMenu>
            <SubMenu key="sub3" icon={<NotificationOutlined />} title="subnav 3">
              <Menu.Item key="9">option9</Menu.Item>
              <Menu.Item key="10">option10</Menu.Item>
              <Menu.Item key="11">option11</Menu.Item>
              <Menu.Item key="12">option12</Menu.Item>
            </SubMenu>
          </Menu>
        </Sider>
        <Content style={{ padding: '0 24px', minHeight: 280 }}>
        
        
        {children}
        
        </Content>
      </Layout>
    </Content>
    <Footer style={{ textAlign: 'center' }}>Ant Design ©2018 Created by Ant UED</Footer>
  </Layout>
  )
}

export default MainLayout
```
</details>

---



<details>
<summary> ____________________ </summary>

Энэ нь уг веб броузерийн мөрөн дээр http://localhost:3000/words гэж ажиллуулахад дуудагдахан ажиллах үүрэгтэй
Мөн энэ хуудсыг дуудахад гадна талаараа өмнөх алхамд үүсгэсэн MainLayout -ийг дуудаж ажиллуулахаар тохиргоог давхар хийж үзье.

**Жишээ нь:**
```
import { Table, Tag, Space,Button } from 'antd';

import { useEffect, useState, useCallback } from "react";
import { useDispatch, useSelector } from "react-redux";
import { pupilJsonDatas } from "../redux/pupil/actionCreator";
import { getAllWords } from "../redux/words/actionCreator";
import actions from "../redux/pupil/actions";


//Layouts
import MainLayout from '../components/layouts/MainLayout'


const columns = [
    {
      title: 'English',
      dataIndex: 'eng',
      key: 'eng'
    },
    {
      title: 'Монгол',
      dataIndex: 'mon',
      key: 'mon',
    },
    {
      title: 'Comment',
      dataIndex: 'comm',
      key: 'comm',
    },
    {
      title: 'Action',
      key: 'action',
      render: (text, record) => (
        <Space size="middle">
          <a>Edit {record.name}</a>
          <a>Delete</a>
        </Space>
      ),
    },
  ];



function allwords() {
  const dispatch = useDispatch();
  const data = useSelector((state) => state.words.list);
  
   
  
    useEffect(() => {
      dispatch(getAllWords());
    }, []);




  return (
    <MainLayout>
    <Space>
    <Button>Үг нэмэх</Button>
    </Space>
    <Table columns={columns} dataSource={data} />
    
    </MainLayout>
  )
}

export default allwords


```
</details>

---

<details>
<summary> ____________________ </summary>

pages/api фолдер дотор 

тухайн фолдер дотор шинэ фордер үүсгээд дотор нь index.js, [id].js -ийг үүсгэж өгнө

**Жишээ нь:** дараах файлуудыг үүсгэнэ. өгөгдлийг өөрчлөх
```
pages/api/dwords/index.js
pages/api/dwords/[id].js
```
</details>

---
<details>
<summary> ____________________________ </summary>

redux фолдер дотор өөрийн үүсгэх redux -ийн нэр бүхийх фолдерийг үүсгэнэ


**Жишээ нь:** дараах файлуудыг үүсгэх
```
redux/dwords/actions.js
redux/dwords/reducers.js
redux/dwords/actionCreater.js

```

**Жишээ нь:** actionCreater.js -ийн кодын хэсгийг хавсаргавал
```
import actions from './actions';
import axios from 'axios'
import {notification } from 'antd';

const { dwordsLoading, dwordsSuccess, dwordsError } = actions;

const openNotification = () => {
  notification.open({
    message: 'Notification Title',
    description:
      'This is the content of the notification. This is the content of the notification. This is the content of the notification.',
    className: 'custom-class',
    style: {
      width: 600,
    },
  });
};


const getAllDWords = () => {
  
  return async dispatch => {
    try {
      dispatch(dwordsLoading());
      await axios.get("http://localhost:3000/api/dwords")
      .then(({data}) => {          
        dispatch(dwordsSuccess(data.list))
        
      });
    } catch (err) {
      dispatch(dwordsError(err));
    }

  };
};


const addDWord = (word) => {
  
  return async dispatch => {
    try {
      dispatch(dwordsLoading());
      await axios.post("http://localhost:3000/api/words",word )
      .then(({data}) => { 
        dispatch(getAllDWords());
        // dispatch(wordsSuccess(data))
      });
    } catch (err) {
      dispatch(wordsError(err));
    }

  };
};


const delDWord = (word) => {
  
  return async dispatch => {
    try {
      //console.log("===========>",word,"<================")
      dispatch(dwordsLoading());
      await axios.delete("http://localhost:3000/api/words",{data:word} )
      .then(({data}) => { 
        dispatch(getAllDWords());
        //dispatch(wordsSuccess(data.list))
      });
    } catch (err) {
      dispatch(wordsError(err));
    }

  };
};


const editDWord = (word) => {
  
  return async dispatch => {
    try {
      console.log("===========>",word,"<================")
      dispatch(wordsLoading());
      await axios.put("http://localhost:3000/api/words",{data:word} )
      .then(({data}) => { 
        dispatch(getAllDWords());
        //dispatch(wordsSuccess(data.list))
      });
    } catch (err) {
      dispatch(dwordsError(err));
    }

  };
};


export {getAllDWords, addDWord,editDWord , delDWord};



```



</details>

---
<details>
<summary> _______________________</summary>

????

**Жишээ нь:**
```
import  WordsReducer  from "./words/reducers";
import  PupilReducer  from "./pupil/reducers";
import DWordsReducer from "./dwords/reducers";  //Энэ хэсэгт import оор оруулж ирэх

export default combineReducers({
  words: WordsReducer,
  Ugs:DWordsReducer, // Энэ хэсэг нэгтгэх үйлдлийг хийж өгөх
  pupil:PupilReducer,
});

```
</details>

---
<details>
<summary> __________________ </summary>

????

**Жишээ нь:**
```
import { getAllDWords } from "../redux/dwords/actionCreator";
...................
...................
<Button onClick={()=>{dispatch(getAllDWords());}}>Ugs</Button>

```
</details>

---
<details>
<summary> ????? </summary>

????

**Жишээ нь:**
```
???
```
</details>

---
<details>
<summary> ????? </summary>

????

**Жишээ нь:**
```
???
```
</details>

---
<details>
<summary> ????? </summary>

????

**Жишээ нь:**
```
???
```
</details>

---

