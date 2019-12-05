<template>
    <v-app>
        <!-- Header -->
        <v-app-bar app class="blue white--text" absolute short fixed clipped-right>
            <router-link to="/">
            <img class="mr-3 mt-1"  :src="require('./assets/MOOR.png')" height="50"/>
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
                <v-menu close-on-content-click="false">
                    <template v-slot:activator="{ on }">
                        <v-btn text class="white--text" @click="" v-on="on" id="cock">Войти</v-btn>
                    </template>
                    <v-card>
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
                                <v-text-field type="text" v-model="email" placeholder="Адрес электронной почты"><br> </v-text-field>
                            </v-list-item>
                            <v-list-item>
                                <v-text-field type="password" v-model="password" placeholder="Пароль"><br></v-text-field>
                            </v-list-item>
                        </v-list>

                        <v-card-actions>
                            <v-btn text to="/register">Зарегестрироваться</v-btn>
                            <v-spacer></v-spacer>
                            <v-btn text @click="menu = false">Отмена</v-btn>
                            <v-btn color="primary" text @click="menu = false">Вход</v-btn>
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
                <v-list-item>
                    <v-list-item-avatar tile>
                        <v-img src="./assets/Igor.png"></v-img>
                    </v-list-item-avatar>

                    <v-list-item-content>
                        <v-list-item-title>Vitas</v-list-item-title>
                        <v-list-item-subtitle>10 Hours of vitas</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                <v-divider></v-divider>
                <v-list-item>
                    <v-list-item-avatar tile>
                        <v-img src="./assets/Igor.png"></v-img>
                    </v-list-item-avatar>

                    <v-list-item-content>
                        <v-list-item-title>Vitas</v-list-item-title>
                        <v-list-item-subtitle>10 Hours of vitas</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                <v-divider></v-divider>
                <v-list-item>
                    <v-list-item-avatar tile>
                        <v-img src="./assets/Igor.png"></v-img>
                    </v-list-item-avatar>

                    <v-list-item-content>
                        <v-list-item-title>Vitas</v-list-item-title>
                        <v-list-item-subtitle>10 Hours of vitas</v-list-item-subtitle>
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
    export default {
        name: 'App',
        data: () => ({}),
        methods: {}
    };
</script>
