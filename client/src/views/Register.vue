<template>
    <div class="sign-up mt-4">
        <h3>Давайте создадим новый аккаунт!</h3>
        <v-text-field type="text" v-model="nickname" placeholder="Никнейм"><br> </v-text-field>
        <v-text-field type="text" v-model="email" placeholder="Адрес электронной почты"><br> </v-text-field>
        <v-text-field type="password" v-model="password" placeholder="Пароль"><br></v-text-field>
        <v-text-field type="password" v-model="passwordconf" placeholder="Повторите пароль"> <br></v-text-field>
        <v-menu ref="menu1" v-model="menu1" :close-on-content-click="false"
                transition="scale-transition" offset-y full-width max-width="290px" min-width="290px">
            <template v-slot:activator="{ on }">
                <v-text-field v-model="birth_day"
                        label="Дата рождения"
                        hint="MM/DD/YYYY format"
                        persistent-hint
                        @blur="date = parseDate(dateFormatted)"
                        v-on="on"
                ></v-text-field>
            </template>
            <v-date-picker v-model="date" no-title @input="menu1 = false"></v-date-picker>
        </v-menu>
        <v-btn x-large  @click="signUp" color="blue" tile dark class="mt-4" to = "/sign-Up">Зарегистрироваться</v-btn>
    </div>
</template>

<script>
    export default {
        name: "Register",
        data() {
            return {
                email: '',
                password: '',
                passwordconf: '',
                nickname:'',
                birth_day:''
            }
        },
        methods:{
            signUp(){

            }
        }
    }
</script>

<style scoped>
    .sign-up {
        margin: auto;
        text-align: center;
        width: 50%;
    }
    input {
        margin: 10px 0;
        width: 20%;
        padding: 15px;
    }
    button {
        margin-top: 10px;
        width: 10%;
        cursor: pointer;
    }
    span {
        display: block;
        margin-top: 20px;
        font-size: 11px;
    }
</style>
