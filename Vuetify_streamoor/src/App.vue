<template>
    <v-app>
        <!-- header-->
        <v-app-bar app class="blue white--text" clipped-left>
            <img class="mr-3" :src="require('./assets/moor.png')" height="60"/>
            <v-toolbar-title class="headline text-uppercase" dark>
                <router-link style="color: white; text-decoration: none" to="/"><span>STREAMOOR</span></router-link>
            </v-toolbar-title>
            <v-toolbar-items class="ml-4">
                <v-btn text class=" white--text" to="/hubs">Хабы</v-btn>
                <v-btn text class=" white--text" to="/info">Инофрмация</v-btn>
                <v-btn text class=" white--text" to="/account">Помощь</v-btn>
            </v-toolbar-items>
            <v-spacer></v-spacer>
            <v-toolbar-items>
                <v-btn text class=" white--text" to="/account">Аккаунт</v-btn>
                <v-btn text class="white--text" @click="logout" id="cock">Войти</v-btn>
            </v-toolbar-items>
        </v-app-bar>

        <!--streamer list-->

        <v-navigation-drawer app clipped>
            <v-list three-line>
                <v-subheader>Сейчас в эфире:</v-subheader>
                <v-divider ></v-divider>
                <v-list-item>
                    <v-list-item-avatar>
                        <img src="./assets/Igor.png">
                    </v-list-item-avatar>
                    <v-list-item-content>
                        <v-list-item-title>Vitas</v-list-item-title>
                        <v-list-item-subtitle>10 Hours of 7th element, what can be better?</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
              <v-divider ></v-divider>
              <v-list-item>
                <v-list-item-avatar>
                  <img src="./assets/moor.png">
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>Moor</v-list-item-title>
                  <v-list-item-subtitle>Main forech</v-list-item-subtitle>
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
    import firebase from 'firebase';

    export default {
        name: 'App',
        data: () => ({
            //
        }),
        methods: {
            logout: function () {
                document.getElementById("cock").innerText = "Войти";
                firebase.auth().signOut().then(() => {
                    this.$router.replace('login')
                });
            }
        }
    };
</script>
