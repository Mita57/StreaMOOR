<template>
    <div class="sign-up mt-4">
        <h3>Создание новой задачи:</h3>
        <v-text-field type="text" v-model="info" placeholder="Общая информация"><br> </v-text-field>
        <v-text-field type="text" v-model="location" placeholder="Место"><br></v-text-field>
        <v-select v-model="select" :items="['Простое','Среднее','Сложное']" item-text="state" item-value="abbr" label="Сложность" persistent-hint return-object single-line></v-select>
        <v-textarea name="input-7-1" filled label="Дополнительня информация" auto-grow ></v-textarea>
        <v-btn x-large  @click="signUp" color="success" dark class="mt-4" to = "/sign-Up">Добавить задачу</v-btn>
    </div>
</template>

<script>
    export default {
        name: "CreateTask"
    }
</script>

<style scoped>
    .sign-up{
        margin: auto;
        text-align: center;
        width: 50%;
    }

</style>