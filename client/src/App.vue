<template>
    <v-app>
        <!-- Header -->
        <v-app-bar app class="blue white--text" absolute short fixed clipped-right>
            <router-link to="/">
                <img class="mr-3 mt-1" :src="require('./assets/MOOR.png')" height="50"/>
            </router-link>
            <v-toolbar-title class="headline text-uppercase" dark>
                <router-link style="color: white; text-decoration: none" to="/"><span>STREAMOOR</span></router-link>
            </v-toolbar-title>
            <v-toolbar-items class="ml-4">
                <v-btn text class=" white--text" to="/hubs">Хабы</v-btn>
                <v-btn text class=" white--text" to="/info">Информация</v-btn>
                <v-btn text class=" white--text" to="/account">Помогите</v-btn>
                <v-text-field type="text" id="search" class="mt-2 ml-10 primary" flat dense solo light placeholder="Поиск"
                              :append-icon="'mdi-magnify'" @click:append="search()">
                </v-text-field>
            </v-toolbar-items>
            <v-spacer></v-spacer>

            <v-toolbar-items>
                <v-menu :close-on-content-click='false'>
                    <template v-slot:activator="{ on }">
                        <v-btn text class="white--text" v-on="on" id="cock">{{user}}</v-btn>
                    </template>
                    <v-card v-model="menu">
                        <v-list>
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title>Войти в ситему</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </v-list>
                        <v-divider></v-divider>
                        <v-list>
                            <v-list-item v-if="auth_result!=''">{{auth_result}}</v-list-item>
                            <v-list-item>
                                <v-text-field type="text" id="email" v-model="email"
                                <v-text-field type="text" id="email" v-model="email"
                                              placeholder="Адрес электронной почты"><br>
                                </v-text-field>
                            </v-list-item>
                            <v-list-item>
                                <v-text-field type="password" id="password" v-model="password" placeholder="Пароль"><br>
                                </v-text-field>
                            </v-list-item>
                        </v-list>

                        <v-card-actions>
                            <v-btn text to="/register" @click="menu=false">Зарегистрироваться</v-btn>
                            <v-spacer></v-spacer>
                            <v-btn text @click="menu=false">Отмена</v-btn>
                            <v-btn color="primary" text @click="menu=false, loginValidation()">Войти</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-menu>
            </v-toolbar-items>
        </v-app-bar>

        <!-- Sidebar -->
        <v-navigation-drawer app id="side">
            <v-list two-line subheader>
                <v-subheader inset style="height: 56px">Сейчас в эфире:</v-subheader>
                <v-divider></v-divider>
                <v-list-item v-for="i in 20">
                        <v-list-item-avatar class="sas" tile>
                            <v-img src="./assets/moorava.jpg"></v-img>
                        </v-list-item-avatar>
                        <v-list-item-content>
                            <v-list-item-title>MoorPK</v-list-item-title>
                            <v-list-item-subtitle>Майн форек гетленч</v-list-item-subtitle>
                            <v-list-item-subtitle>Подкасты</v-list-item-subtitle>
                        </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-content>
            <router-view/>
        </v-content>
    </v-app>
</template>

<script>
    import axios from 'axios';
    import router from "./router";

    export default {
        name: 'App',
        data() {
            return {
                user: 'Войти',
                channels: [],
                auth_result: ''
            }
        },
        methods: {
            loginValidation: function () {
                //input validation
                const aw = this;
                let passwordFlag = false;
                let emailFlag = false;
                if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(document.getElementById('email').value)) {
                    emailFlag = true;
                    document.getElementById('email').style.backgroundColor = '#424242';
                } else {
                    document.getElementById('email').style.backgroundColor = 'darkred';
                    emailFlag = false;
                }
                if (document.getElementById('password').value.length >= 4) {
                    passwordFlag = true;
                    document.getElementById('password').style.backgroundColor = '#424242';
                } else {
                    document.getElementById('password').style.backgroundColor = 'darkred';
                    passwordFlag = false;
                }


                if (passwordFlag && emailFlag) {
                    login(document.getElementById('email').value, document.getElementById('password').value);
                }

                function login(email, pwrd) {
                    axios({
                        headers: {
                            'Access-Control-Allow-Origin': '*',
                            'Content-Type': 'application/json',
                        },
                        method: 'post',
                        url: 'http://localhost:5000/login',
                        data: {
                            email: email,
                            password: pwrd
                        },
                    }).then(function (response) {
                        if (response.data.result == 'fail') {
                            aw.auth_result = 'Неправильное имя пользователя или пароль';
                        }
                        else {
                            localStorage.user = response.data.result;
                            aw.user = response.data.result;
                        }
                    })
                        .catch(function (response) {
                            //handle error
                            console.log(response);
                        })
                }

            },
            search(){
                if(document.getElementById('search').value.length > 0) {
                    router.push('search/' + document.getElementById('search').value);
                }
            }
        }
    };
</script>

<style>
    a {
        text-decoration: none;
        color: white;
    }

    #search {
        width: 500px;
    }

    .v-navigation-drawer__content::-webkit-scrollbar {
        width: 6px;
        background-color: #F5F5F5;
    }
    .v-navigation-drawer__content::-webkit-scrollbar-thumb {
        box-shadow: inset 0 0 5px grey;
        background: dodgerblue;
    }
</style>
