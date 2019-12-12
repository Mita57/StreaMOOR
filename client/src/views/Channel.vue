<template>
    <v-container class="justify-center ma-0 pa-0">
        <!--channel tabs-->
        <v-tabs v-model="tab" height="50px" class="" dark icons-and-text>
            <v-tabs-slider></v-tabs-slider>
            <v-tab href="" class="flex-row">
                <img src="../assets/Igor.png" class="mr-2 ml-n2 mt-1" height="40px">
                {{nickname}}
            </v-tab>

            <v-tab href="">
                Эфир
            </v-tab>

            <v-tab href="">
                Записи
            </v-tab>
            <v-divider></v-divider>
            <v-btn class="success mt-2" tile>Подписаться</v-btn>
            <v-tab disabled>Подписчиков: {{subscibers}}</v-tab>
        </v-tabs>
        <!--chat-->
        <v-navigation-drawer app clipped right>
            <v-list two-line subheader>
                <v-subheader inset>Чат:</v-subheader>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>10 Hours of vitas</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
            <div class="">
                <v-text-field type="text" placeholder="Сообщение"  class="sas pa-2 mb-n4"></v-text-field>
            </div>
        </v-navigation-drawer>
        <v-responsive :aspect-ratio="16/9" class=" ma-8 mt-2 white">
            <img src="http://localhost:5000/video_feed" id="stream">
        </v-responsive>
        <v-container fluid>
            <v-layout wrap  class="ml-5 mt-n8">
                <v-flex>
                    <div>
                        <div>
                            {{desc}}
                        </div>
                        <div>
                            {{hub}}
                        </div>
                    </div>
                </v-flex>
                <div class="mr-5 viewers">
                    {{viewers}}
                </div>
            </v-layout>
        </v-container>
    </v-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Channel",
        data() {
            return {
                nickname: 'Cuberian',
                subscibers: 1337228,
                desc:'Учимся пользоваться гитом с Игорешей',
                hub:'Наука и обучение',
                viewers: 228
            }
        },
        methods: {
            async getInfo(){
                const rw = this;
                const capitalize = (s) => {
                    if (typeof s !== 'string') return '';
                    return s.charAt(0).toUpperCase() + s.slice(1);
                }
                let nick = (window.location.href.split('/')[5]);
                await axios.get('http://localhost:5000/channel?nickname=' + nick)
                    .then(function (res) {
                        console.log(res);
                        rw.nickname = res.data[0][0];
                        rw.subscibers = res.data[0][1];
                        rw.desc = res.data[0][2];
                        rw.hub = capitalize(res.data[0][3]);
                    })
                    .catch(function (res) {
                        //handle error
                        console.log(res);
                    })
            }
        },
        mounted(){
            this.getInfo();
        },
    }

</script>

<style scoped>
.viewers{
    color:dodgerblue;
}
.sas{
    position: absolute;
    bottom: 0px;
    width: 100%;
 }
    #stream{
        position: absolute;
        height: 100%;
        width: 100%;
    }
</style>
