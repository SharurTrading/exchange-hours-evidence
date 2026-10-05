$(document).ready(function () {
    $('ul#filter a').click(function () {
        $(this).css('outline', 'none');
        $('ul#filter .current').removeClass('current');
        $(this).parent().addClass('current');

        var filterVal = $(this).attr("id");

        if (filterVal == 'all-announcements') {
            $('tbody#body tr.hidden').fadeIn('fast').removeClass('hidden');
        } else if (filterVal == 'shareholdings'){
            $('tbody#body tr').each(function () {
                if (!(($(this).find('td:eq(3)').text() == "RELINT") || ($(this).find('td:eq(3)').text() == "SSH") || ($(this).find('td:eq(3)').text() == "SSHO")))  {
                    $(this).fadeOut('fast').addClass('hidden');
                }else {
                    $(this).fadeIn('fast').removeClass('hidden');
                }
            });
        } else if (filterVal == 'communications/results/meetings'){
            $('tbody#body tr').each(function () {
                if (!(($(this).find('td:eq(3)').text() == "ADDRESS") || ($(this).find('td:eq(3)').text() == "MEETING") || ($(this).find('td:eq(3)').text() == "S/HOLDER") || ($(this).find('td:eq(3)').text() == "ANNREP") || ($(this).find('td:eq(3)').text() == "INTERM") || ($(this).find('td:eq(3)').text() == "HALFYR") || ($(this).find('td:eq(3)').text() == "FLLYR") || ($(this).find('td:eq(3)').text() == "QUARTER") || ($(this).find('td:eq(3)').text() == "MONTHLY") || ($(this).find('td:eq(3)').text() == "FORECAST")))  {
                    $(this).fadeOut('fast').addClass('hidden');
                }else {
                    $(this).fadeIn('fast').removeClass('hidden');
                }
            });
        } else if (filterVal == 'corporate-actions'){
            $('tbody#body tr').each(function () {
                if (!(($(this).find('td:eq(3)').text() == "ALLOT") || ($(this).find('td:eq(3)').text() == "APPNDX7") || ($(this).find('td:eq(3)').text() == "BONUS") || ($(this).find('td:eq(3)').text() == "BUYBACK") || ($(this).find('td:eq(3)').text() == "CALL") || ($(this).find('td:eq(3)').text() == "CAPREC") || ($(this).find('td:eq(3)').text() == "FLLYR") || ($(this).find('td:eq(3)').text() == "QUARTER") || ($(this).find('td:eq(3)').text() == "CONV") || ($(this).find('td:eq(3)').text() == "DIVIDEND") || ($(this).find('td:eq(3)').text() == "ENTITLE") || ($(this).find('td:eq(3)').text() == "EXERCISE") || ($(this).find('td:eq(3)').text() == "INTEREST") || ($(this).find('td:eq(3)').text() == "PLACE") || ($(this).find('td:eq(3)').text() == "RIGHT") || ($(this).find('td:eq(3)').text() == "S/A") || ($(this).find('td:eq(3)').text() == "DRP")))  {
                    $(this).fadeOut('fast').addClass('hidden');
                }else {
                    $(this).fadeIn('fast').removeClass('hidden');
                }
            });
        } else if (filterVal == 'price-sensitive'){
            $('tbody#body tr').each(function () {
                if($(this).find('a.price-sensitive').length <= 0){
                    $(this).fadeOut('fast').addClass('hidden');
                }else{
                    $(this).fadeIn('fast').removeClass('hidden');
                }
            });
        }
        return false;
    });
});
