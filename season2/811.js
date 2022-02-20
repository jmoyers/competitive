/**
 * @param {string[]} cpdomains
 * @return {string[]}
 */
var subdomainVisits = function(cpdomains) {
  const dc = {};
  
  for (const domain of cpdomains) {
    const [count, full_domain] = domain.split(" ");
    
    const domains = full_domain.split(".");
    
    if (domains.length) {
      let record = domains.pop();
      dc[record] = dc[record] ? dc[record] + Number(count) : Number(count);
      
      while (domains.length) {
        record = domains.pop() + "." + record;
        dc[record] = dc[record] ? dc[record] + Number(count) : Number(count);
      }
    }
  }
  
  const ans = [];
  
  for (const [k, v] of Object.entries(dc)) {
    ans.push(v + " " + k);
  }
  
  return ans;
};
