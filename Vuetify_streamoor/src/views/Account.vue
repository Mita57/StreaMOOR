<template>
    <v-container class="justify-center" >
        <v-row no-gutters class="justify-center align-center">
            <v-col cols="12" sm="6" md="8" >
                <v-card class="mx-auto order-2" outlined>
                    <v-list-item three-line>
                        <div class="text-center">
                            <v-img :src="require('../assets/pic4.jpg')" max-width="125"/>
                            <v-btn x-small color="success" dark>Поменять аватар</v-btn>
                        </div>
                        <v-list-item-content class="ml-5">
                            <v-list-item-title class="headline mb-1">57thrasher57@gmail.com</v-list-item-title>
                            <v-list-item-subtitle>nickname: we_wanna_win_makerthon</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                    <v-card-actions>
                    </v-card-actions>
                </v-card>
                <v-card class="mx-auto mt-4 order-3" tile>
                    <v-list >
                        <v-subheader> Отзывы: work in progress...</v-subheader>
                    </v-list>
                </v-card>
            </v-col>
            <v-col cols="10" md="4">
                <v-card class="pa-2 ml-4 order-1 mt-4" outlined tile>
                    Рейтинг: <v-rating v-model="rating" class="d-inline-block" background-color="purple lighten-3" color="purple" value=3.4 small></v-rating> <br>
                    Заданий выполнено : 228 <br>
                    Заданий создано: 1337 <br>
                    <v-btn color="success" dark large width="170" class="mt-4 ml-2" to = "/createTask">Создать задание</v-btn>
                    <v-btn color="success" dark large width="170" class="ml-2 mt-4" to = "/createTask">Настройки</v-btn>
                    <v-btn color="success"  class=" ml-2 mt-4" dark large width="170">Мои задания</v-btn>
                </v-card>

            </v-col>
        </v-row>
    </v-container>
</template>

<script>
//import firebase from 'firebase';
//var user = firebase.auth().currentUser;
    export default {
        name: "Account",
        computed:{
            getUsers(){
                this.$store.dispatch('usersModule/openDBChannel');
                return this.$store.getters['usersModule/getUsers'];
            },

        }
    }

</script>

<style scoped>

</style>