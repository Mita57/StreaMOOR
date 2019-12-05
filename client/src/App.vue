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
                    <v-btn text class="white--text" @click="" v-on="on" id="cock">Войти</v-btn>
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
