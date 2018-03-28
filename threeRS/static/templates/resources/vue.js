
// Layout Component definition
Vue.component('page-layout', {
    template: `
    <div class='row justify-content-center'>
      <div class='col-lg-12'>
        <p class='lead'>Instructions</p>

        {{ text }}
        <br/>

        <input class="form-control" v-model="text">

        <br/>
        
        <div id="container"></div>


      </div>
    </div>
  `,
    // data - returns an object representing the component state
    data () {
        return {
            text: 'Search',
        }
    }
});

