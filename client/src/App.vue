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
                <v-btn text class=" white--text" to="/info">Инофрмация</v-btn>
                <v-btn text class=" white--text" to="/account">Помогите</v-btn>
            </v-toolbar-items>
            <v-spacer></v-spacer>
            <v-toolbar-items>
                <v-menu  :close-on-content-click='false'>
                    <template v-slot:activator="{ on }">
                        <v-btn text class="white--text"  v-on="on" id="cock">{{nickname}}</v-btn>
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
                            <v-list-item>
                                <v-text-field type="text" id="email" v-model="email" placeholder="Адрес электронной почты"><br>
                                </v-text-field>
                            </v-list-item>
                            <v-list-item>
                                <v-text-field type="password" id="password" v-model="password" placeholder="Пароль"><br>
                                </v-text-field>
                            </v-list-item>
                        </v-list>

                        <v-card-actions>
                            <v-btn text to="/register" @click="menu=false">Зарегестрироваться</v-btn>
                            <v-spacer></v-spacer>
                            <v-btn text @click="menu=false">Отмена</v-btn>
                            <v-btn color="primary" text @click="menu=false, loginValidation()"">Вход</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-menu>
            </v-toolbar-items>
        </v-app-bar>

        <!-- Sidebar -->
        <v-navigation-drawer app>
            <v-list two-line subheader>
                <v-subheader inset style="height: 56px">Сейчас в эфире:</v-subheader>
                <v-divider></v-divider>
                <v-list-item v-for="i in 20">
                    <router-link to="/channel">
                    <v-list-item-avatar class="sas" tile>
                        <v-img src="./assets/Igor.png" class=""></v-img>
                    </v-list-item-avatar>
                    <v-list-item-content>
                        <v-list-item-title>Игорь</v-list-item-title>
                        <v-list-item-subtitle>Учимся пользоваться гитом</v-list-item-subtitle>
                        <v-list-item-subtitle>Креатив</v-list-item-subtitle>
                    </v-list-item-content>
                    </router-link>
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

    export default {
        name: 'App',
        data() {
            return {
                nickname: 'Войти',
                channels: [],
            }
        },
        methods: {
            loginValidation(){
                //input validation
                let passwordFlag  = false;
                let emailFlag = false;
                if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(document.getElementById('email').value)){
                    emailFlag = true;
                    document.getElementById('password').style.backgroundColor = '#424242';
                }
                else{
                    document.getElementById('email').style.backgroundColor = 'darkred';
                }
                if(document.getElementById('password').value.length > 4){
                    passwordFlag = true;
                    document.getElementById('password').style.backgroundColor = '#424242';
                }
                else{
                    document.getElementById('password').style.backgroundColor = 'darkred';
                }


                if(passwordFlag && emailFlag){
                    login();
                }

                async function login() {
                    let formData = new FormData();
                    formData.set('email', document.getElementById('email').value);
                    formData.set('password', document.getElementById('pasword').value);
                    await axios({
                        method : 'post',
                        url : 'localhost:5000/login',
                        data : formData
                    }).then(function (response) {
                        this.nickname = response.data.nickname;
                    })
                        .catch(function (response) {
                            //handle error
                            console.log(response);
                            alert('Kernel panic: not sycning')
                        })
                }

            },
        }
    };
</script>

<style>
    a{
        text-decoration: none;
        color: white;
    }
</style>
