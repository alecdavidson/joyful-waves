/**
 * Created by SalvatoreBottiglieri on 1/20/15.
 */

$('body').scrollspy({
    target: '.bs-docs-sidebar',
    offset: 70
});
$("#sidebar").affix({
    offset: {
      top: 230
    }
});
