<template>
  <v-app>
    <v-app-bar app class="blue white--text">
      <img class="mr-3" :src="require('./assets/moor.png')" height="60"/>
      <v-toolbar-title class="headline text-uppercase" dark>
        <router-link style="color: white; text-decoration: none" to="/"><span >STREAMOOR</span></router-link>
      </v-toolbar-title>
      <v-toolbar-items class="ml-4">
        <v-btn text class=" white--text" to="/hubs">Хабы</v-btn>
        <v-btn text class=" white--text" to="/info">Инофрмация</v-btn>
        <v-btn text class=" white--text" to="/account">Помощь</v-btn>
      </v-toolbar-items>
      <v-spacer></v-spacer>
      <v-toolbar-items >
        <v-btn text class=" white--text" to="/account">Аккаунт</v-btn>
        <v-btn text class="white--text"  @click="" id="cock">Войти</v-btn>
      </v-toolbar-items>
    </v-app-bar>
    <v-navigation-drawer app >
      <v-list two-line subheader>
        <v-subheader inset>Сейчас в эфире:</v-subheader>

        <v-list-item>
          <v-list-item-avatar>
            <v-img src="assets/Igor.png"></v-img>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title >Vitas</v-list-item-title>
            <v-list-item-subtitle >10 Hours of vitas</v-list-item-subtitle>
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
export default {
  name: 'App',
  data: () => ({

  }),
  methods: {

  }
};
</script>
