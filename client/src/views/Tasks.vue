<template>
    <div class="tasks">
        <v-card class="mx-auto sas" v-for="item in getTasks" :id="'id'+item.info">
            <div :class="getDificulty(item.type)" :id="'hdr'+item.info" >
                <p >{{typeDificulty(item.type)}}</p>
            </div>
            <div class="d-flex flex-no-wrap justify-space-between sas">
                <div>
                    <v-card-title>{{item.info}}</v-card-title>
                    <v-card-subtitle>{{item.desc}}</v-card-subtitle>
                    <v-card-actions>
                        <v-btn large>Написать</v-btn>
                        <v-btn large color="blue lighten-4 " @click='takeTask(item.info)'>Взять</v-btn>
                        <v-spacer></v-spacer>
                    </v-card-actions>
                    <v-expand-transition>
                        <div v-show="show" >
                            <v-img :src="require('../assets/Igor.png')" class="float-right"  max-width="125"/>
                            <v-card-title>Заказчик</v-card-title>
                            <v-card-subtitle>Cuberian</v-card-subtitle>
                            <v-card-subtitle>Крупкин Игорь Андреевич</v-card-subtitle>
                            <v-card-subtitle>Cuberian</v-card-subtitle>
                            <v-card-subtitle>themess@inbox.ru</v-card-subtitle>
                            <v-card-subtitle>88005553535</v-card-subtitle>
                        </div>
                    </v-expand-transition>
                </div>
                <div>
                    <v-card-title>{{toDateTime(item.submit_time.seconds)}}<br></v-card-title>
                    <v-card-subtitle>{{item.master}}<br></v-card-subtitle>
                    <v-card-title>Цена: {{item.price}}</v-card-title>
                </div>
            </div>
        </v-card>
    </div>


</template>

<script>

    export default {
        name: "tasks",
        data() {
            return {
                show: false
            }
        },
        computed: {
            getTasks() {
                this.$store.dispatch('worksModule/openDBChannel');
                return this.$store.getters['worksModule/getTasks'];

            },
            getUsers(){
                this.$store.dispatch('usersModule/openDBChannel');
                return this.$store.getters['usersModule/getUsers'];
            },
            getUserById(uid){
                //this.$store.dispatch('usersModule/openDBChannel');
                return this.$store.getters['usersModule/getUserById'](uid);
            }
        }
        , methods: {
            toDateTime(secs) {
                var t = new Date(1970, 0, 1);
                t.setSeconds(secs);
                var day = t.getDay();
                if (day < 10) {
                    day = "0" + day;
                }
                var month = t.getMonth();
                if (month < 10) {
                    month = "0" + month;
                }
                var outism = "" + day + "." + month + '|' + t.getHours() + ":" + t.getMinutes();
                if (t.getMinutes() == 0) {
                    outism += '0';
                }
                return outism;
            },
            getDificulty(type) {
                let colors = ['light-green accent-3', 'yellow accent-4', 'orange accent-4'];
                return colors[type] + ' header';
            },
            typeDificulty(type) {
                let difs = ['Просто', 'Средне', 'Сложно'];
                return difs[type];
            },
            takeTask(taskName) {
                var myNodeList = document.getElementsByClassName("sas");
                document.getElementById('hdr' + taskName).className = 'taken';
                for(var i = 0; i < myNodeList.length; i++){
                    if(myNodeList[i].classList.contains('taken')){
                        continue;
                    }
                    myNodeList[i].style.display = 'None';
                }
                console.log(myNodeList.length);
                document.getElementById('id' + taskName).style.display = 'Block';
                this.show = true;
            }
        }
    }
</script>

<style scoped>
    .mx-auto {
        max-width: 97%;
        margin-top: 20px;
    }

    .mx-auto .header {
        background-color: forestgreen;
        height: 70px;
    }

    .mx-auto .header p {
        color: white;
        font-family: Helvetica, serif;
        font-weight: bold;
        font-size: 20pt;
        padding-top: 15px;
        padding-left: 20px;
    }
    .taken{
        height: 70%;
        background-color: deepskyblue;
        color: white;
        font-family: Helvetica, serif;
        font-weight: bold;
        font-size: 20pt;
        padding-top: 15px;
        padding-left: 20px;
        height: 70px;
    }
</style>