<template>
    <div class="sign-up mt-4">
        <h3>Давайте создадим новый аккаунт!</h3>
        <v-text-field type="text" v-model="nickname" placeholder="Никнейм"><br> </v-text-field>
        <v-text-field type="text" v-model="email" placeholder="Адрес электронной почты"><br> </v-text-field>
        <v-text-field type="password" v-model="password" placeholder="Пароль"><br></v-text-field>
        <v-text-field type="password" v-model="passwordconf" placeholder="Повторите пароль"> <br></v-text-field>
        <v-btn x-large  @click="signUp" color="success" dark class="mt-4" to = "/sign-Up">Зарегистрироваться</v-btn>
        <span>Или вернуться к форме <router-link to="/login">авторизации</router-link>.</span>
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
            }
        },
        methods:{
            signUp(){

            }
        }
    }
</script>

<style scoped>

</style>
