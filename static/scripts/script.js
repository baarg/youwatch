const item = $(".maincon"); 
const contant = $(".footercon");
const barShadow = $(".shadow");
item.click(function(){

    const this_item = $(this).parent().find(contant);
    const this_barShadow = $(this).parent().find(barShadow);
 
    // this_item.slideToggle();
    this_item.slideToggle();
    this_barShadow.slideToggle();
   
}) 


const icon = $('.icon');
const show = $('.show');
const sera = $('.searchin');
icon.click(function(){
    show.fadeToggle();
})

ser.click(function(){
    sera.slideToggle();
})

