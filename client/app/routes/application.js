import Ember from 'ember';

//import OsfAgnosticAuthRouteMixin from 'ember-osf/mixins/osf-agnostic-auth-route';

//export default Ember.Route.extend(OsfAgnosticAuthRouteMixin, {
export default Ember.Route.extend({

    store: Ember.inject.service(),
    session: Ember.inject.service(),

    model() {
        //if (this.get('session.isAuthenticated')) {
        //    return this.get('store').findRecord('user', 'me');
        //}
    }
});
